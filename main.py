from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

@app.get("/{file_path:path}")
def read_file(file_path: str):
    file_path = os.path.join(os.getcwd(), file_path)
    if os.path.exists(file_path):
        return {"message": f"File {file_path} exists"}
    else:
        return {"error": f"File {file_path} not found"}