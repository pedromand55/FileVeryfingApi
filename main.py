#FileSharingAPI lavet af Lukas (pedromand55 på github)
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

print("FileSharingAPI v1.2")
print("Starting API...")

app = FastAPI()

@app.get("/{file_path:path}")
def read_file(file_path: str):
    file_path = os.path.join(os.getcwd(), file_path)
    if os.path.exists(file_path):
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == ".xml":
            return {"message": f"File {file_path} exists"}
        else:
            return {"error": f"Only XML files are allowed"}
    else:
        return {"error": f"File {file_path} not found"}