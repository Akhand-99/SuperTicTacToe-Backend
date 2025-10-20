def create_room(room_id, room_name, room_password):
    return {
        room_id: {
            "room_id": room_id,
            "room_name": room_name,
            "room_password": room_password,
            "players": [],
            "game_state": {
                "mainBoardCellList": [None, None, None, None, None, None, None, None, None],
                "smallBoards": [
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                {
                    "boardCellList": [None, None, None, None, None, None, None, None, None],
                    "wonBy": None,
                },
                ],
                "currentMarkerToPlace": "X",
                "wonBy": None, #"X" || "O" || "Nobody" || None. If None, game is not finished.
                "activeBoardNumber": 0, # 0 means, marker can be placed on any board (For initial move and moves where the board to be played on is full, or already won)
            }
        }
    }