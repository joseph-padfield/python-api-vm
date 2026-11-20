from flask import Flask, request

app = Flask(__name__)


@app.get("/api/health")
def health():
    return {"status": "ok"}

@app.get("/api/hello")
def hello():
    try:
        name = request.args.get("name").strip()

        if not name:
            return {"error": "The name query parameter is required."}, 400

        else:
            return {"message": f"Hello, {name}!"}

    except:
        return {"error": "The name query parameter is required."}, 400
        
