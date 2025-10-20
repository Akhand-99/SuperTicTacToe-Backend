from fastapi import FastAPI
import uuid
from rooms_logic import room

app = FastAPI()

# rooms_dict = {
#     "1": {
#         "room_id": 1,
#         "room_name": "Newton and Leibniz's Super Battle",
#         "room_password": "NewtonMadeCalculusFirst",
#         "players": [
#             {
#                 "player_id": 101,
#                 "player_name": "Newton"
#             },
#             {
#                 "player_id": 102,
#                 "player_name": "Leibniz"
#             }
#         ],
#         "game_state": {"<Game State>"}
#     },
#     "2": {
#         "room_id": 2,
#         "room_name": "Alice and Bob's Super Battle",
#         "room_password": "AliceInWonderland",
#         "players": [
#             {
#                 "player_id": 103,
#                 "player_name": "Alice"
#             },
#             {
#                 "player_id": 104,
#                 "player_name": "Bob"
#             }
#         ],
#         "game_state": {"<Game State>"}
#     }
# } # room_ids are keys, room_info are values

rooms_dict = {}

@app.get("/ping")
async def ping():
    return {"message": "pong!"}

@app.post("/room_creation")
async def room_creation():
    room_id = uuid.uuid4()
    # Write logic here to get room_name and password from request body.
    # Gemini says FastAPI recommended approach is to make a Pydantic Model for the
    # Request body and use it as param of this endpoint func, it will take care
    # of validation and parsing, etc. Have a quick look on this and continue
    # building out the logic.
    
    # room.create_room(room_id, room_name, room_password)
