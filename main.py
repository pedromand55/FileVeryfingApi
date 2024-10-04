#Made by Lukas
import os
from fastapi import FastAPI, Path
from fastapi.responses import JSONResponse

app = FastAPI(
    title="File Existence Checker API",
    description="An API to check if a file exists on the server.",
    version="1.0.0"
)


# Define the number of cores
num_cores = 4

# Define the file existence check function
def check_file_exists(file_path):
    file_path = os.path.join(os.getcwd(), file_path)
    if os.path.exists(file_path):
        return {"message": f"File {file_path} exists"}
    else:
        return {"error": f"File {file_path} not found"}

@app.get("/{file_path:path}")
async def read_file(file_path: str = Path(..., description="The path to the file to check")):
    """
    Check if a file exists on the server.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        JSONResponse: A JSON response indicating whether the file exists or not.
    """
    # Create a ThreadPoolExecutor with the specified number of cores
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        # Submit the file existence check to the executor
        future = executor.submit(check_file_exists, file_path)
        
        # As the file existence check completes, store the result
        try:
            result = future.result()
        except Exception as e:
            return JSONResponse(status_code=500, content={"error": f"Error checking file {file_path}: {e}"})

    return JSONResponse(status_code=200, content=result)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
