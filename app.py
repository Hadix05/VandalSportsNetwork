from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from queries import get_all_players, get_all_teammates

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


# To run this server: uvicorn app:app --reload
