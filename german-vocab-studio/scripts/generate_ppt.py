from pathlib import Path
import sys

# Ensure project root is on sys.path so `from app...` imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.ppt_service import generate_ppt


generate_ppt()
