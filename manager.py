from fastapi import WebSocket
from typing import List

from services import connect_logic

class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        # dealing with incomming connections here
        await connect_logic(self, websocket)
    async def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def broadcast(self, data: str):
        # broadcasting data to all connected clients
        for connection in self.connections:
            await connection.send_json(data)
