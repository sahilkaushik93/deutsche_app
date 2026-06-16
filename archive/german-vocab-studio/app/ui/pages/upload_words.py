from pathlib import Path
import sys

# Ensure project root is on sys.path for Streamlit import context
root = Path(__file__).resolve().parent
for _ in range(6):
	if (root / 'requirements.txt').exists() or (root / 'README.md').exists():
		break
	root = root.parent
sys.path.insert(0, str(root))

import streamlit as st
from app.utils.file_utils import ensure_dir


def app():
	st.header('Upload Words Excel')
	uploaded = st.file_uploader('Upload an Excel file with columns Word, Meaning, Synonyms, Sentences, Image', type=['xlsx'])
	if uploaded is not None:
		dest = Path('data') / 'excel'
		ensure_dir(dest)
		out_path = dest / uploaded.name
		with open(out_path, 'wb') as f:
			f.write(uploaded.getbuffer())
		st.success(f'Saved to {out_path}')


if __name__ == '__main__':
	app()
