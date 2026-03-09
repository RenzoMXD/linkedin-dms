from fastapi import FastAPI

app = FastAPI(title="Desearch DMs", version="0.0.1")


@app.get("/health")
def health():
    return {"ok": True}
