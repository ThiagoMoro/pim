from operations import add_player, list_players, get_player, give_item, level_up

def print_menu():
  print("\n-- Player Inventory Manager --")
  print("1. Add player")
  print("2. List players")
  print("3. Show player")
  print("4. Give item")
  print("5. Level up player")
  print("6. Quit")

  def menu_loop():
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        if choice == '1':
            name = input("Enter new player's name: ").strip()
            ok, result = add_player(name)
            if ok:
                print(f"Player '{name}' added.")
            else:
                if result == "exists":
                    print("That player already exists.")
                elif result == "empty_name":
                    print("Name cannot be empty.")
                else:
                    print("Could not add player.")
        elif choice == '2':
            players = list_players()
            if not players:
                print("No players found.")
            else:
                print("Players:")
                for n, p in sorted(players.items()):
                    print(f" - {n} (level {p['level']}, {len(p['inventory'])} items)")
        elif choice == '3':
            name = input("Enter player's name to show: ").strip()
            p = get_player(name)
            if not p:
                print(f"No player named '{name}'.")
            else:
                print(f"Name: {p['name']}")
                print(f"Level: {p['level']}")
                print("Inventory:")
                if p['inventory']:
                    for i, it in enumerate(p['inventory'], 1):
                        print(f"  {i}. {it}")
                else:
                    print("  (empty)")
        elif choice == '4':
            name = input("Enter player's name to give an item: ").strip()
            item = input("Enter item name: ").strip()
            ok, res = give_item(name, item)
            if ok:
                print(f"Item '{item}' given to {name}.")
            else:
                if res == "no_player":
                    print("Player not found.")
                elif res == "empty_item":
                    print("Item name cannot be empty.")
                else:
                    print("Could not give item.")
        elif choice == '5':
            name = input("Enter player's name to level up: ").strip()
            ok, res = level_up(name)
            if ok:
                print(f"{name} is now level {res['level']}.")
            else:
                print("Player not found.")
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")