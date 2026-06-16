from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Word:
    word: str
    meaning: str
    synonyms: List[str] = field(default_factory=list)
    sentences: List[str] = field(default_factory=list)
    image: Optional[str] = None

    @classmethod
    def from_row(cls, row: dict):
        # Accept either pandas Series or dict-like
        get = row.get if hasattr(row, 'get') else (lambda k, d=row: d[k] if k in d else None)
        synonyms = get('Synonyms') or get('synonyms') or ''
        sentences = get('Sentences') or get('sentences') or ''
        return cls(
            word=(get('Word') or get('word') or '').strip(),
            meaning=(get('Meaning') or get('meaning') or '').strip(),
            synonyms=[s.strip() for s in str(synonyms).split(',') if s.strip()],
            sentences=[s.strip() for s in str(sentences).split('|') if s.strip()] or [s.strip() for s in str(sentences).split('.') if s.strip()],
            image=(get('Image') or get('image') or None)
        )
