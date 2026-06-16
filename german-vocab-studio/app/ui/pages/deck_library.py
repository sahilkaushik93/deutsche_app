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


def app():
	st.header('Deck Library')
	folder = Path('data') / 'generated' / 'ppt'
	if not folder.exists():
		st.info('No generated decks yet.')
		return
	files = list(folder.glob('*.pptx'))
	for f in files:
		st.write(f.name)


if __name__ == '__main__':
	app()
