tournament = {
    "India": [
        {"name": "Rohit", "runs": 250, "wickets": 1},
        {"name": "Virat Kohli", "runs": 300, "wickets": 3},
        {"name": "Bumrah", "runs": 40, "wickets": 8}
    ],
    "Australia": [
        {"name": "Smith", "runs": 270, "wickets": 1},
        {"name": "Warner", "runs": 260, "wickets": 0},
        {"name": "Starc", "runs": 30, "wickets": 10}
    ]
}

player_score = lambda p: p["runs"] + p["wickets"] * 20

team_scores = {team: sum(player_score(p) for p in players)
               for team, players in tournament.items()}

best_team, best_player_data = max(
    ((team, max(players, key=player_score)) for team, players in tournament.items()),
    key=lambda x: player_score(x[1])
)
best_player = best_player_data["name"]
best_score = player_score(best_player_data)


winner = (lambda i, a: "India" if i > a else ("Australia" if a > i else "Match Tied"))(
    team_scores["India"], team_scores["Australia"]
)

print("=== Match Summary ===")
print("India Total Score:", team_scores["India"])
print("Australia Total Score:", team_scores["Australia"])
print("\nWinner Team:", winner)
print("Player of the Series:", best_player, "from", best_team, f"(Score: {best_score})")
