from fastapi import FastAPI, HTTPException

app = FastAPI()


trains = [
    {
        "train_id": "ICE101",
        "destination": "Frankfurt",
        "status": "On Time"
    },
    {
        "train_id": "ICE202",
        "destination": "Berlin",
        "status": "Delayed"
    }
]


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "train-api"
    }

@app.get("/trains")
def get_trains():
    return trains


@app.get("/trains/{train_id}")
def get_train(train_id: str):

    for train in trains:
        if train["train_id"] == train_id:
            return train

    raise HTTPException(
        status_code=404,
        detail="Train not found"
    )
