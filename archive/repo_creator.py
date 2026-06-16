from pathlib import Path

PROJECT_NAME = "german-vocab-studio"

FOLDERS = [
    "app",
    "app/config",
    "app/ui",
    "app/ui/pages",
    "app/services",
    "app/models",
    "app/templates",
    "app/templates/ppt",
    "app/templates/narration",
    "app/utils",
    "data",
    "data/excel",
    "data/images",
    "data/generated",
    "data/generated/ppt",
    "data/generated/video",
    "data/generated/audio",
    "data/generated/thumbnails",
    "data/backups",
    "scripts",
    "tests",
    "docs"
]

FILES = {
    "README.md": "# German Vocabulary Studio\n",

    "requirements.txt":
        """pandas
openpyxl
python-pptx
pillow
streamlit
moviepy
""",

    ".gitignore":
        """__pycache__/
*.pyc
.env
.venv
data/generated/
""",

    "app/main.py":
        """def main():
    print("German Vocabulary Studio")

if __name__ == "__main__":
    main()
""",

    "app/config/settings.py":
        """PROJECT_NAME = "German Vocabulary Studio"
VERSION = "1.0.0"
""",

    "app/config/layout_config.json":
        """{
  "word_font_size": 28,
  "meaning_font_size": 18,
  "synonym_font_size": 18,
  "sentence_font_size": 16,
  "max_sentences": 3
}
""",

    "app/ui/streamlit_app.py":
        """import streamlit as st

st.title("German Vocabulary Studio")
""",

    "app/ui/pages/upload_words.py":
        "# Upload words page\n",

    "app/ui/pages/generate_ppt.py":
        "# Generate ppt page\n",

    "app/ui/pages/deck_library.py":
        "# Deck library page\n",

    "app/services/excel_service.py":
        """import pandas as pd

def read_excel(path):
    return pd.read_excel(path)
""",

    "app/services/ppt_service.py":
        """from pptx import Presentation

def generate_ppt():
    pass
""",

    "app/services/image_service.py":
        """def process_image():
    pass
""",

    "app/services/animation_service.py":
        """def apply_animation():
    pass
""",

    "app/services/narration_service.py":
        """def generate_script():
    pass
""",

    "app/services/video_service.py":
        """def generate_video():
    pass
""",

    "app/models/word.py":
        """class Word:
    pass
""",

    "app/models/deck.py":
        """class Deck:
    pass
""",

    "app/templates/ppt/placeholders.json":
        """{
  "WORD_BOX": "word",
  "MEANING_BOX": "meaning",
  "SYNONYM_BOX": "synonyms",
  "SENTENCE_BOX": "sentences",
  "IMAGE_BOX": "image"
}
""",

    "app/templates/narration/script_template.txt":
        """Word: {word}

Meaning:
{meaning}

Synonyms:
{synonyms}

Sentence:
{sentence}
""",

    "app/utils/file_utils.py":
        "# file utilities\n",

    "app/utils/image_utils.py":
        "# image utilities\n",

    "app/utils/ppt_utils.py":
        "# ppt utilities\n",

    "app/utils/logger.py":
        """import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
""",

    "data/excel/words.xlsx": "",

    "scripts/generate_ppt.py":
        """from app.services.ppt_service import generate_ppt

generate_ppt()
""",

    "scripts/generate_video.py":
        """from app.services.video_service import generate_video

generate_video()
""",

    "scripts/validate_excel.py":
        "# validate excel\n",

    "scripts/bulk_import.py":
        "# bulk import\n",

    "tests/test_excel.py":
        "# excel tests\n",

    "tests/test_ppt.py":
        "# ppt tests\n",

    "tests/test_video.py":
        "# video tests\n",

    "docs/architecture.md":
        "# Architecture\n",

    "docs/workflow.md":
        "# Workflow\n",

    "docs/template_guide.md":
        "# PPT Template Guide\n"
}


def create_repo():
    root = Path(PROJECT_NAME)

    root.mkdir(exist_ok=True)

    for folder in FOLDERS:
        (root / folder).mkdir(parents=True, exist_ok=True)

    for file_path, content in FILES.items():
        full_path = root / file_path

        full_path.parent.mkdir(parents=True, exist_ok=True)

        if not full_path.exists():
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(content)

    print(f"\nRepository created successfully:\n{root.resolve()}")


if __name__ == "__main__":
    create_repo()