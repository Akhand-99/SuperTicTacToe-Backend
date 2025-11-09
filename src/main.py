from fastapi import FastAPI, WebSocket
import uuid
from rooms_logic import room
from pydantic import BaseModel

class RoomDetailsFromClient(BaseModel):
    room_name: str
    room_password: str

class JoinRoomRequest(BaseModel):
    player_id: str
    player_name: str
    room_id: str
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
    
    room_id_str = str(room_id)
    created_room_dict = room.create_room(room_id_str, room_name, room_password)
    global rooms_dict
    rooms_dict = rooms_dict | created_room_dict # Merging the 2 dicts. This is re-assignment not in-place modification.
    return {"room_id": room_id}

@app.websocket("/join_room")
async def join_room(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        
        join_room_request = JoinRoomRequest.model_validate_json(data)
        player_id = join_room_request.player_id
        player_name = join_room_request.player_name
        room_id = join_room_request.room_id
        room_password = join_room_request.room_password

        room_state = rooms_dict[room_id]
        current_room_player_count = len(room_state["players"])

        if current_room_player_count == 2:
            await websocket.send_json({"message": "Room is already full!", "isError": True})
        elif room_id in rooms_dict and room_password == rooms_dict[room_id]["room_password"]:
            player_details = {"player_id": player_id, "player_name": player_name}
            room_state["players"].append(player_details)
            room_join_success_dict = {"message": "Room Joined Successfully!", "roomState": rooms_dict[room_id], "isError": False}
            await websocket.send_json(room_join_success_dict)
        else:
            await websocket.send_json({"message": "Invalid Credentials.", "isError": True})
    
