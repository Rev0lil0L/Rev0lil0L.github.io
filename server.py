from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/", StaticFiles(directory="./"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=55562, reload=False)