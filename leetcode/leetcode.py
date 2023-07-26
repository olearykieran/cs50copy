import random

teams = [
    "Team A",
    "Team B",
    "Team C",
    "Team D",
    "Team E",
    "Team F",
    "Team G",
    "Team H",
    "Team I",
    "Team J",
    "Team K",
    "Team L"
]

scores = {}

for team in teams:
    score = random.randint(0, 100)
    scores[team] = score

for team, score in scores.items():
    print(f"{team}: {score}")