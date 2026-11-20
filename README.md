# Python API on a VM

A small Flask API for learning how to run a Python service on an Ubuntu Server VM and call it from a Mac.

## Local setup

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Start Flask with `python -m flask --app app run`. Run tests with `python -m pytest`.

## Endpoints

| Request | Status | JSON response |
| --- | --- | --- |
| `GET /api/health` | `200 OK` | `{"status": "ok"}` |
| `GET /api/hello?name=Jo` | `200 OK` | `{"message": "Hello, Jo!"}` |

## Example requests

Once the API is running on the VM at `192.168.64.5`, replace `PORT` with the port Flask is listening on and run these commands from your Mac.

```sh
curl 'http://192.168.64.5:PORT/api/health'
curl 'http://192.168.64.5:PORT/api/hello?name=Jo'
```
