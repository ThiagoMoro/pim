import json
import os

DATA_FILE = 'players.json'

def load_players():
    """Return players dict loaded from players.json or an empty dict."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        try:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
        except json.JSONDecodeError:
            return {}

def save_players(data):
    """Save the players dict to players.json (pretty printed)."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)