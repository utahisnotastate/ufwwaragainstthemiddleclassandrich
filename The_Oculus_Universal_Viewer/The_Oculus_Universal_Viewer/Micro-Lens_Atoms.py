"""
Micro-Lens (Atoms) component for The_Oculus_Universal_Viewer.
Cloud-optional implementation with safe fallbacks when BigQuery is unavailable.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

# Optional numpy for any numeric utilities
try:
    import numpy as np  # type: ignore
    _HAS_NUMPY = True
except Exception:
    np = None  # type: ignore
    _HAS_NUMPY = False

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


class MicroLensAtoms:
    def __init__(self, dataset_id: str = 'atomic_data', table_id: str = 'atom_properties',
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

    def fetch_atomic_data(self, element_symbol: str) -> Dict[str, Dict[str, Any]]:
        """Fetch atomic properties for the given symbol. Returns a dict keyed by element name."""
        client = self._get_client()
        if client is None:
            # Fallback stub data
            stub: Dict[str, Dict[str, Any]] = {
                'Hydrogen': {
                    'symbol': 'H',
                    'atomic_number': 1,
                    'atomic_mass': 1.008,
                    'electronic_configuration': '1s1',
                },
                'Helium': {
                    'symbol': 'He',
                    'atomic_number': 2,
                    'atomic_mass': 4.0026,
                    'electronic_configuration': '1s2',
                },
            }
            return {k: v for k, v in stub.items() if v['symbol'].lower() == element_symbol.lower()}

        query = (
            f"SELECT element, symbol, atomic_number, atomic_mass, electronic_configuration "
            f"FROM `{self.dataset_id}.{self.table_id}` WHERE LOWER(symbol) = '{element_symbol.lower()}'"
        )
        try:
            results = client.query(query)
            out: Dict[str, Dict[str, Any]] = {}
            for row in results:
                out[row.element] = {
                    'symbol': row.symbol,
                    'atomic_number': row.atomic_number,
                    'atomic_mass': float(row.atomic_mass) if row.atomic_mass is not None else None,
                    'electronic_configuration': row.electronic_configuration,
                }
            return out
        except Exception as e:
            logger.warning("BigQuery query failed, using fallback: %s", e)
            return self.fetch_atomic_data(element_symbol) if self._get_client() is None else {}

    def parse_electronic_config(self, config_str: str) -> str:
        """Return a lightly normalized configuration string (placeholder parser)."""
        if not config_str:
            return ''
        # Normalize whitespace and casing
        return ' '.join(str(config_str).split())

    def process_atomic_data(self, element_symbol: str) -> Dict[str, Any]:
        """Return a simplified view of atom properties for display/analysis."""
        raw = self.fetch_atomic_data(element_symbol)
        if not raw:
            return {}
        element_name = next(iter(raw.keys()))
        entry = raw[element_name]
        return {
            'element': element_name,
            'symbol': entry.get('symbol'),
            'atomic_number': entry.get('atomic_number'),
            'atomic_mass': entry.get('atomic_mass'),
            'electronic_configuration': self.parse_electronic_config(entry.get('electronic_configuration', '')),
        }


if __name__ == '__main__':
    lens = MicroLensAtoms()
    for sym in ('H', 'He'):
        print(sym, '=>', lens.process_atomic_data(sym))
