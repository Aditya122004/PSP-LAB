def create_team(team_name):
    team={}
    n=int(input(f"Enter number of players in {team_name}"))
    print(f"Enter player details for {team_name}")
    for i in range(n):
        name=input(f"Player {i+1} name:")
        runs=int(input(f"runs scored by {name}:"))
        wickets=int(input(f"Wickets taken by {name}"))
        team[name]={"runs":runs,"wickets":wickets}
    return team
def best_batsman(team):
    best_player=max(team,key=lambda x:team[x]["runs"])
    print(f"Best Batsman:{best_player} with {team[best_player]['runs']} runs")

def best_bowler(team):
    best_player=max(team,key=lambda x:team[x]["wickets"])
    print(f"Best Bowler:{best_player} with {team[best_player]['wickets']} wickets")
def total_score(team):
    total_runs=sum(player["runs"] for player in team.values())
    total_wickets=sum(player["wickets"] for player in team.values())
    return total_runs,total_wickets
def compare_team(team1,team2):
    runs1,wickets1=total_score(team1)
    runs2,wickets2=total_score(team2)

    print(f"Team A->runs:{runs1},Wickets:{wickets1}")
    print(f"Team B->runs:{runs2},Wickets:{wickets2}")
    if runs1>runs2:
        print("Team A wins")
    elif runs1<runs2:
        print("Team B wins")
    else:
        print("Tie")
team1=create_team("Team A")
team2=create_team("Team B")
print("Team A:")
best_batsman(team1)
best_bowler(team1)
print("Team B:")
best_batsman(team2)
best_bowler(team2)
print("Resutl:")
compare_team(team1,team2)  
    
