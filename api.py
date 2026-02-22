from fastapi import FastAPI, HTTPException
from moviebox_api import MovieAuto
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home():
    return {"status": "online", "message": "Welcome to Abel's Movie Engine. Use /search?q=movie"}

@app.get("/search")
async def search(q: str):
    try:
        auto = MovieAuto()
        # auto.run returns (movie_file_obj, subtitle_file_obj)
        movie_file, _ = await auto.run(q)
        
        if not movie_file:
            raise HTTPException(status_code=404, detail="No movie found")

        return {
            "title": movie_file.title,
            "year": getattr(movie_file, 'release_year', 'Unknown'),
            "url": movie_file.stream_url,
            "filename": movie_file.filename
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
