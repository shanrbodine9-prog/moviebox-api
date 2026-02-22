from fastapi import FastAPI
from moviebox_api import MovieAuto
import uvicorn
import os

app = FastAPI()

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
