# 🎮 Player Inventory Manager (Python Study Project)

A simple, modular Command-Line Interface (CLI) application built to manage player data, levels, and inventories. This project was developed to practice fundamental Python concepts in a real-world scenario (game backend logic).

## 🚀 Key Features
- **Player Creation**: Dynamic creation of player profiles.
- **Leveling System**: Update player levels with automated feedback.
- **Inventory Management**: Add and track items for each player.
- **Data Persistence**: All data is saved in a `players.json` file.
- **automated Logging**: Every action is time-stamped and recorded in `log.txt`.

## 📁 Project Structure (Modular Architecture)
The project is divided into specialized modules, following best practices for code organization:

- `main.py`: The entry point of the application.
- `cli.py`: User interface and menu interaction.
- `operations.py`: Core business logic (managing levels and items).
- `storage.py`: Handles JSON reading and writing.
- `logger.py`: Manages the automated record of system events.

## 🛠️ Concepts Applied
- **File I/O**: Practical use of `open()`, `with` statement, and different modes (`'r'`, `'w'`, `'a'`).
- **Data Structures**: Complex dictionaries and lists.
- **JSON Module**: Serialization and deserialization of data.
- **Modularity**: Importing functions across different Python files.
- **Persistence**: Ensuring data is not lost afterclosing the program.

## 💻 How to Run
1. Clone this repository:  
    git clone git@github.com:ThiagoMoro/pim.git 
2. Navigate to the project folder:  
    cd player-inventory-manager  
3. Run the application:  
    python main.py  
   
## 📜 License
This project is for educational purposes. Feel free to use and modify it!
