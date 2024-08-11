from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from starlette.websockets import WebSocketDisconnect

from templates.client import html

from services import update_board

from manager import ConnectionManager

import json

app = FastAPI()


manager = ConnectionManager()

@app.get("/")
def index():
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # here we are waiting for an oncomming message from clients
            data = await websocket.receive_text()
            data = json.loads(data)
            # precessing the incomming message
            await update_board(manager, data)
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
    finally:
        pass