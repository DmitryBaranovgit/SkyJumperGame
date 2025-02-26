import json
from settings import LEADERBOARD_FILE

def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_leaderboard(score):
    leaderboard = load_leaderboard()
    leaderboard.append(score)
    leaderboard = sorted(leaderboard, reverse = True)[:5] # Топ-5 лучших результатов

    with open(LEADERBOARD_FILE, "w") as file:
        json.dump(leaderboard, file)