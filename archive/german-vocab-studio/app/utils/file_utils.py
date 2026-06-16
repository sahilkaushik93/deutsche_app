import os
from pathlib import Path


def ensure_dir(path: str):
	Path(path).mkdir(parents=True, exist_ok=True)


def safe_path(path: str) -> str:
	return str(Path(path))


def write_binary(path: str, data: bytes):
	ensure_dir(os.path.dirname(path) or '.')
	with open(path, 'wb') as f:
		f.write(data)


def read_text(path: str) -> str:
	with open(path, 'r', encoding='utf-8') as f:
		return f.read()
