from typing import List
from .word import Word
import pandas as pd


class Deck:
    def __init__(self, title: str, words: List[Word]):
        self.title = title
        self.words = words

    @classmethod
    def from_excel(cls, path: str, title: str = "German Words"):
        df = pd.read_excel(path)
        words: List[Word] = []
        for _, row in df.fillna('').iterrows():
            w = Word.from_row(row)
            if w.word:
                words.append(w)
        return cls(title=title, words=words)

    def __len__(self):
        return len(self.words)

    def to_list(self):
        return self.words
