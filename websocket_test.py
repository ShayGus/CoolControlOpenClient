import json
import websocket
import _thread
import time
import rel
import ast


def on_message(ws, message):
    print(message)
    d = json.loads(message)
    if d["type"] == "ping":
        ws.send('{"type":"pong"}')
        print('{"type":"pong"}')


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://api.coolremote.net/api/v1", on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close
    )

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    ws.send(
        '{"type":"authenticate","content":{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYxZjhkYmFlYThhMzFjMTk2NmIxZWNlYyIsImlhdCI6MTY0OTc2MDQxNiwiZXhwIjoxNjgxMzE4MDE2fQ.RLwz3qiZgLBRwHYpPQGrYtPC3t34axQBh2C7pP_wdVU"}}'
    )
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
