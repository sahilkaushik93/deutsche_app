import pandas as pd
from pathlib import Path
from app.models.deck import Deck
from app.utils.logger import logger


REQUIRED_COLUMNS = ['Word', 'Meaning']


def read_excel(path: str) -> pd.DataFrame:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f'Excel file not found: {path}')
    suffix = p.suffix.lower()
    engine = None
    if suffix in ('.xlsx', '.xlsm', '.xltx', '.xltm'):
        engine = 'openpyxl'
    elif suffix == '.xls':
        engine = 'xlrd'
    try:
        if engine:
            return pd.read_excel(path, engine=engine)
        return pd.read_excel(path)
    except Exception as e:
        logger.error(f'Failed to read Excel file {path}: {e}')
        raise


def validate_columns(df: pd.DataFrame) -> bool:
    cols = [c for c in df.columns]
    for rc in REQUIRED_COLUMNS:
        if rc not in cols:
            logger.error(f"Missing required column: {rc}")
            return False
    return True


def load_deck_from_excel(path: str, title: str = 'German Words') -> Deck:
    df = read_excel(path)
    if not validate_columns(df):
        raise ValueError('Excel missing required columns')
    return Deck.from_excel(path, title=title)
