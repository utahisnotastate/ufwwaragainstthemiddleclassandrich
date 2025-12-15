"""
Macro-Lens (Galaxies) component for The_Oculus_Universal_Viewer.
Cloud-optional implementation with safe fallbacks when BigQuery/pandas are unavailable.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

# Optional Google BigQuery
try:
    from google.cloud import bigquery  # type: ignore
    _HAS_BIGQUERY = True
except Exception:
    bigquery = None  # type: ignore
    _HAS_BIGQUERY = False

# Optional pandas
try:
    import pandas as pd  # type: ignore
    _HAS_PANDAS = True
except Exception:
    pd = None  # type: ignore
    _HAS_PANDAS = False

logger = logging.getLogger(__name__)
if not logger.handlers:
    logging.basicConfig(level=logging.INFO)


class MacroLensGalaxies:
    """Macro view processor for galaxy data with cloud-optional querying."""

    def __init__(self, dataset_id: str = "astronomy_data", table_id: str = "galaxy_catalog",
                 project_id: Optional[str] = None) -> None:
        self.dataset_id = dataset_id
        self.table_id = table_id
        self.project_id = project_id

    def _get_client(self):
        if not _HAS_BIGQUERY:
            return None
        try:
            return bigquery.Client(project=self.project_id) if self.project_id else bigquery.Client()
        except Exception as e:
            logger.warning("BigQuery client unavailable: %s", e)
            return None

    def fetch_galaxy_data(self) -> List[Dict[str, Any]]:
        """Fetch galaxy data from BigQuery when available, else provide synthetic sample data."""
        client = self._get_client()
        if client is None:
            # Fallback sample dataset with redshift values
            return [
                {"name": "NGC 1300", "redshift": 0.00526},
                {"name": "Messier 87", "redshift": 0.00436},
                {"name": "Andromeda", "redshift": 0.0009},
                {"name": "Sombrero", "redshift": 0.003416},
            ]

        query = f"SELECT * FROM `{self.dataset_id}.{self.table_id}` LIMIT 5000"
        try:
            job = client.query(query)
            rows = list(job)
            data = [dict(row) for row in rows]
            return data
        except Exception as e:
            logger.warning("BigQuery query failed, using fallback: %s", e)
            return [
                {"name": "NGC 1300", "redshift": 0.00526},
                {"name": "Messier 87", "redshift": 0.00436},
                {"name": "Andromeda", "redshift": 0.0009},
                {"name": "Sombrero", "redshift": 0.003416},
            ]

    @staticmethod
    def process_galaxy_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Compute a simple distance metric from redshift and sort ascending."""
        processed: List[Dict[str, Any]] = []
        for row in data:
            redshift = row.get("redshift")
            try:
                z = float(redshift)
            except (TypeError, ValueError):
                continue
            # Simplified Hubble's Law proxy (units not literal)
            distance = 3.086e19 * z / 70.0
            newrow = dict(row)
            newrow["distance"] = distance
            processed.append(newrow)
        processed.sort(key=lambda r: r.get("distance", float("inf")))
        return processed

    def get_macro_view(self) -> List[Dict[str, Any]]:
        """Fetch raw data and return processed macro view."""
        raw = self.fetch_galaxy_data()
        return self.process_galaxy_data(raw)


if __name__ == "__main__":
    macro_lens = MacroLensGalaxies()
    macro_view = macro_lens.get_macro_view()
    for row in macro_view[:5]:
        print(row)
