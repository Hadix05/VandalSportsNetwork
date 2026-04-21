from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from queries import get_all_players, get_all_teammates, get_players_by_stats, get_players_by_team, get_all_teams

app = FastAPI()

# This allows your frontend HTML file to talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/players")
def players():
    return get_all_players()


@app.get("/teammates/{player_id}")
def teammates(player_id: int):
    return get_all_teammates(player_id)

@app.get("/players/filter")
def filter_players(min_pts: float = 0, min_reb: float = 0, min_ast: float = 0):
    return get_players_by_stats(min_pts, min_reb, min_ast)

@app.get("/teams")
def teams():
    return get_all_teams()

@app.get("/teams/{team_name}/players")
def players_by_team(team_name: str):
    return get_players_by_team(team_name)

# To run this server: uvicorn app:app --reload
