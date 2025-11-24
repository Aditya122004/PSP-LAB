tournament={
    "India":
                [
                    {"name":"Rahul","runs":250,"wickets":1},
                    {"name":"Virat","runs":300,"wickets":3},
                    {"name":"Jasprit","runs":40,"wickets":10}
                ],
    "Australia":
                [
                    {"name":"Smith","runs":270,"wickets":1},
                    {"name":"Head","runs":260,"wickets":0},
                    {"name":"Cummins","runs":30,"wickets":11}
                ]
    }
india_score=0
australia_score=0
best_player=""
best_team=""
best_score=0

for team,players in tournament.items():
    for player in players:
        score=player["runs"]+player["wickets"]*30
        if team=="India":
            india_score+=score
        else:
            australia_score+=score
        if score > best_score:
            best_score=score
            best_player=player["name"]
            best_team=team
if india_score>australia_score:
    winner="India"
elif australia_score>india_score:
    winner="Australia"
else:
    winner="Match tied"
print("Match Summary")
print("India Total Score=",india_score)
print("Australia Total Score=",australia_score)
print("Winner Team:",winner)
print("Player of the series:",best_player,"From",best_team,f"score:{best_score}")

                
