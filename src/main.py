from fastapi import FastAPI
import uuid
from rooms_logic import room
from pydantic import BaseModel

class RoomDetailsFromClient(BaseModel):
    room_name: str
    room_password: str

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
async def room_creation(room_details: RoomDetailsFromClient):
    room_id = uuid.uuid4()
    room_name = room_details.room_name
    room_password = room_details.room_password
    
    created_room_dict = room.create_room(room_id, room_name, room_password)
    global rooms_dict
    rooms_dict = rooms_dict | created_room_dict # Merging the 2 dicts. This is re-assignment not in-place modification.
    return {"room_id": room_id}