from moviebox_api import MovieAuto, Config

@app.get("/search")
async def search(q: str):
    try:
        # Tell the engine to look like a real Chrome browser
        config = Config(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        auto = MovieAuto(config=config)
        movie_file, _ = await auto.run(q)
        # ... rest of your code
