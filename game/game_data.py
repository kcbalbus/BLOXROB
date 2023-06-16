import json

# Przykładowa struktura danych dla wyników i ułożeń plansz
game_data = {
    "easy": {
        "best_score": 100,
        "board_state": [[1, 2], [3, 4]]
    },
    "medium": {
        "best_score": 200,
        "board_state": [[2, 1], [4, 3]]
    },
    "hard": {
        "best_score": 300,
        "board_state": [[4, 3], [2, 1]]
    }
}

# Zapisywanie danych do pliku JSON
with open("game_data.json", "w") as file:
    json.dump(game_data, file)

# Odczytywanie danych z pliku JSON
with open("game_data.json", "r") as file:
    loaded_data = json.load(file)

# Przykład odczytywania danych
best_score_easy = loaded_data["easy"]["best_score"]
board_state_medium = loaded_data["medium"]["board_state"]

print(best_score_easy)  # Wyświetli: 100
print(board_state_medium)  # Wyświetli: [[2, 1], [4, 3]]