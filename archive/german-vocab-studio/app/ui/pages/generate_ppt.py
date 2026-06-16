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
from app.services.ppt_service import generate_ppt


def app():
	st.header('Generate PowerPoint')
	if st.button('Generate PPT from default Excel'):
		try:
			out = generate_ppt()
			st.success(f'Generated {out}')
		except Exception as e:
			st.error(str(e))


if __name__ == '__main__':
	app()
