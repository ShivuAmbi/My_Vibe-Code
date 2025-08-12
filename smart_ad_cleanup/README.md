# Smart AD Cleanup Assistant

This tool analyzes Active Directory objects (users, computers, groups) and uses AI to recommend cleanup actions for stale or inactive accounts.

## Features
- Pulls AD objects
- Uses AI to classify objects as active/inactive/stale
- Generates cleanup recommendations

## Usage
1. Install requirements: `pip install -r requirements.txt`
2. Run: `python main.py`

## Customization
- Integrate with your AD environment by replacing the placeholder AD pull logic in `main.py`.
