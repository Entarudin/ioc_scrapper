import uvicorn
from fastapi import FastAPI

from app.src.ui.rest.http.v1 import router as scrapping_request_routes


app = FastAPI()
app.include_router(scrapping_request_routes)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
