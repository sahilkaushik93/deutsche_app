from pathlib import Path
import sys

# Ensure project root is on sys.path so `from app...` imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.video_service import generate_video


generate_video()
