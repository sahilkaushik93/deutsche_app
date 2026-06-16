from pathlib import Path
import sys

# Ensure project root is on sys.path for Streamlit import context
p = Path(__file__).resolve().parent
root = p
for _ in range(6):
	if (root / 'requirements.txt').exists() or (root / 'README.md').exists():
		break
	root = root.parent
sys.path.insert(0, str(root))

import streamlit as st

st.title("German Vocabulary Studio")
