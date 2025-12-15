"""
Chrono-Lens (Time) component for The_Oculus_Universal_Viewer.
Cloud-optional time navigation with safe fallbacks when BigQuery is unavailable.
"""

from __future__ import annotations

import datetime as _dt
import logging
from typing import Any, Dict, List, Optional

# Optional Google BigQuery
try:
    from google.cloud import bigquery  # type: ignore
    _HAS_BIGQUERY = True
except Exception:
    bigquery = None  # type: ignore
    _HAS_BIGQUERY = False

logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)


class ChronoLens:
    def __init__(self, project_id: Optional[str] = None, dataset_table: str = "your_dataset.your_table",
                 timestamp_column: str = "timestamp_column") -> None:
        self.project_id = project_id
        self.dataset_table = dataset_table
        self.timestamp_column = timestamp_column

    def _get_client(self):
        if not _HAS_BIGQUERY:
            return None
        try:
            return bigquery.Client(project=self.project_id) if self.project_id else bigquery.Client()
        except Exception as e:
            logger.warning("BigQuery client unavailable: %s", e)
            return None

    def _run_query(self, where_clause: str, order: str) -> List[Dict[str, Any]]:
        client = self._get_client()
        if client is None:
            # Fallback: synthesize some rows
            now = _dt.datetime.now()
            rows = []
            for i in range(5):
                rows.append({
                    "id": i,
                    self.timestamp_column: (now + _dt.timedelta(days=i if order == 'ASC' else -i)).isoformat(),
                    "value": 100 + i if order == 'ASC' else 100 - i,
                })
            return rows
        query = (
            f"SELECT * FROM `{self.dataset_table}` WHERE {where_clause} "
            f"ORDER BY {self.timestamp_column} {order} LIMIT 1000"
        )
        try:
            job = client.query(query)
            return [dict(row) for row in job]
        except Exception as e:
            logger.warning("BigQuery query failed, using fallback: %s", e)
            return self._run_query("TRUE", order)

    def rewind_time(self, days: int) -> List[Dict[str, Any]]:
        target_date = (_dt.datetime.now() - _dt.timedelta(days=int(days))).strftime('%Y-%m-%d')
        where = f"DATE({self.timestamp_column}) <= '{target_date}'"
        return self._run_query(where, order="DESC")

    def fast_forward_time(self, days: int) -> List[Dict[str, Any]]:
        target_date = (_dt.datetime.now() + _dt.timedelta(days=int(days))).strftime('%Y-%m-%d')
        where = f"DATE({self.timestamp_column}) >= '{target_date}'"
        return self._run_query(where, order="ASC")


if __name__ == "__main__":
    chrono = ChronoLens()
    print("Past Data:", chrono.rewind_time(30)[:3])
    print("Future Data:", chrono.fast_forward_time(30)[:3])
