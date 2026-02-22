from fastapi import FastAPI
from moviebox_api import MovieAuto
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import asyncio

app = FastAPI()

# This part is CRITICAL: It lets Lovable talk to your Render server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
async def search(q: str):
    try:
        auto = MovieAuto()
        movie_file, _ = await auto.run(q)
        return {"title": movie_file.title, "url": movie_file.stream_url}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
