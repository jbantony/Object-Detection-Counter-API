from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to object detection API"}





if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 5000))
    uvicorn.run("object_detector_api:app",host="0.0.0.0", port=PORT)