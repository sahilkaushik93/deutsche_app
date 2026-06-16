# German Vocabulary Studio

## Overview

German Vocabulary Studio is a personal productivity application designed to automate the creation of German vocabulary learning presentations and, in future phases, educational videos.

The goal is to eliminate repetitive PowerPoint work while maintaining complete control over content quality and slide design.

Instead of manually creating slides for every word, the user simply provides:

* Word
* Meaning
* Synonyms
* Example Sentences
* Image

The application automatically generates PowerPoint slides based on a predefined template.

---

# Current MVP Scope

### Input

Excel File

| Word     | Meaning   | Synonyms             | Sentences                  | Image        |
| -------- | --------- | -------------------- | -------------------------- | ------------ |
| Abfahren | To depart | losfahren, wegfahren | Der Zug fährt um 8 Uhr ab. | abfahren.jpg |

### Output

PowerPoint Presentation

```text
German Words #1

Slide 1
Slide 2
Slide 3
Slide 4
Slide 5
```

Each slide follows the predefined PowerPoint template.

---

# Future Vision

Current:

```text
Excel
 ↓
PowerPoint
```

Future:

```text
Excel
 ↓
PowerPoint
 ↓
Narration
 ↓
Voice Generation
 ↓
Animations
 ↓
MP4 Video
```

---

# Repository Structure

```text
german-vocab-studio/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── layout_config.json
│   │
│   ├── ui/
│   │   ├── streamlit_app.py
│   │   │
│   │   └── pages/
│   │       ├── upload_words.py
│   │       ├── generate_ppt.py
│   │       └── deck_library.py
│   │
│   ├── services/
│   │   ├── excel_service.py
│   │   ├── ppt_service.py
│   │   ├── image_service.py
│   │   ├── animation_service.py
│   │   ├── narration_service.py
│   │   └── video_service.py
│   │
│   ├── models/
│   │   ├── word.py
│   │   └── deck.py
│   │
│   ├── templates/
│   │   ├── ppt/
│   │   │   ├── german_template.pptx
│   │   │   └── placeholders.json
│   │   │
│   │   └── narration/
│   │       └── script_template.txt
│   │
│   └── utils/
│       ├── file_utils.py
│       ├── image_utils.py
│       ├── ppt_utils.py
│       └── logger.py
│
├── data/
│   │
│   ├── decks/
│   │   ├── German_A1_001.xlsx
│   │   ├── German_A1_002.xlsx
│   │   └── German_B1_001.xlsx
│   │
│   ├── images/
│   │   ├── abfahren.jpg
│   │   ├── ankommen.jpg
│   │   └── ...
│   │
│   ├── generated/
│   │   ├── ppt/
│   │   ├── video/
│   │   ├── audio/
│   │   └── thumbnails/
│   │
│   └── backups/
│
├── scripts/
│   ├── generate_ppt.py
│   ├── generate_video.py
│   ├── validate_excel.py
│   └── bulk_import.py
│
├── tests/
│   ├── test_excel.py
│   ├── test_ppt.py
│   └── test_video.py
│
└── docs/
    ├── architecture.md
    ├── workflow.md
    └── template_guide.md
```

---

# Component Responsibilities

## app/services/excel_service.py

Responsibilities:

* Read Excel files
* Validate columns
* Load vocabulary records
* Prepare slide data

---

## app/services/ppt_service.py

Responsibilities:

* Load PowerPoint template
* Replace placeholders
* Insert images
* Generate slides
* Export PowerPoint file

---

## app/services/image_service.py

Responsibilities:

* Validate image files
* Resize images
* Crop images
* Maintain aspect ratio

---

## app/services/narration_service.py

Future Module

Responsibilities:

* Generate narration script
* Create explanations
* Generate memory tricks

---

## app/services/video_service.py

Future Module

Responsibilities:

* Convert slides into video
* Add transitions
* Add audio narration
* Export MP4

---

# PowerPoint Template Design

The application is designed around a master PowerPoint template.

Instead of hardcoding coordinates in Python, the template contains named placeholders.

Example:

```text
WORD_BOX
MEANING_BOX
SYNONYM_BOX
SENTENCE_BOX
IMAGE_BOX
```

The application locates these placeholders and injects data dynamically.

Benefits:

* No code changes when redesigning slides
* Consistent branding
* Consistent formatting
* Easier maintenance

---

# MVP Workflow

```text
User
 │
 ▼
Excel File
 │
 ▼
Read Vocabulary Data
 │
 ▼
Load PPT Template
 │
 ▼
Replace Placeholders
 │
 ▼
Insert Images
 │
 ▼
Generate Slides
 │
 ▼
Export PPT
 │
 ▼
Download PPT
```

---

# Future Workflow

```text
User
 │
 ▼
Excel File
 │
 ▼
Generate PPT
 │
 ▼
Generate Narration
 │
 ▼
Generate Audio
 │
 ▼
Apply Animations
 │
 ▼
Create Video
 │
 ▼
Export MP4
```

---

# Installation

```bash
git clone <repository-url>

cd german-vocab-studio

pip install -r requirements.txt
```

---

# Run Streamlit Application

```bash
streamlit run app/ui/streamlit_app.py
```

---

# Planned Features

## Phase 1

* Excel Upload
* Image Upload
* PPT Generation

## Phase 2

* Image Auto-Cropping
* Image Suggestions

## Phase 3

* Narration Script Generation

## Phase 4

* Voice Generation

## Phase 5

* PPT to Video Conversion

## Phase 6

* Fully Automated German Vocabulary Video Creation

---

# Long-Term Goal

Create a single platform where vocabulary content can be entered once and automatically transformed into:

* PowerPoint Presentations
* Educational Videos
* Narrated Lessons
* YouTube-Ready Content

while preserving complete control over design, branding, and learning methodology.