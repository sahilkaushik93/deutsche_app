from pathlib import Path
import sys

# Ensure project root is on sys.path so `from app...` imports work
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.excel_service import read_excel, validate_columns


def main(path: str):
	df = read_excel(path)
	ok = validate_columns(df)
	if ok:
		print('Excel looks good')
	else:
		print('Excel is missing required columns')


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Usage: python validate_excel.py path/to/file.xlsx')
	else:
		main(sys.argv[1])
