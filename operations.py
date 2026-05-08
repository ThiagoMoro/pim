from storage import load_players, save_players
from logger import log_action

def make_player(name: str):
  return {"name": name, "level": 1, "inventory": []}

def add_player(name: str):
  data = load_players()
  if not name:
    return False, "empty name"
  if name in data:
    return False, "exists"
  data[name] = make_player(name)
  save_players(data)
  log_action(f"Added player '{name}'")
  return True, data[name]

def list_players():
  data = load_players()
  return data # dict of players

def get_player(name: str):
  data = load_players()
  return data.get(name)

def give_item(name: str, item: str):
  data = load_players()
  player = data.get(name)
  if player is None:
    return False, "no_player"
  if not item:
    return False, "empty item"
  player['inventory'].append(item)
  save_players(data)
  log_action(f"Gave '{item}' to player '{name}'")
  return True, player

def level_up(name: str):
  data = load_players()
  player = data.get(name)
  if player is None:
    return False, "no_player"
  player['level'] += 1
  save_players(data)
  log_action(f"Leveled up player '{name}' to level {player['level']}")
  return True, player
