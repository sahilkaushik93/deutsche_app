from pathlib import Path
from app.utils.image_utils import validate_image, resize_to_fit


def process_image(image_name: str, max_width: int = 800, max_height: int = 800, src_folder: str = 'data/images', dest_folder: str = 'data/generated/thumbnails') -> str:
    src = Path(src_folder) / image_name
    dest = Path(dest_folder) / image_name
    if not src.exists():
        raise FileNotFoundError(f'Image not found: {src}')
    if not validate_image(str(src)):
        raise ValueError(f'Invalid image: {src}')
    resize_to_fit(str(src), max_width, max_height, str(dest))
    return str(dest)
