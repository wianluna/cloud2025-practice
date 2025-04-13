from flask import Flask, request, jsonify
import redis
import random

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def home():
    return "🎬 MovieBucket — To Watch & Watched"

@app.route("/add", methods=["POST"])
def add_movie():
    data = request.get_json()
    title = data.get("title")
    genre = data.get("genre")
    if not title or not genre:
        return "Missing 'title' or 'genre'", 400
    r.sadd(f"to_watch:{genre}", title)
    return f"🎥 Added '{title}' to 'to watch' list under genre '{genre}'"

@app.route("/to_watch/<genre>", methods=["GET"])
def get_to_watch(genre):
    movies = list(r.smembers(f"to_watch:{genre}"))
    return jsonify({genre: movies})

@app.route("/random/<genre>", methods=["GET"])
def get_random(genre):
    movies = list(r.smembers(f"to_watch:{genre}"))
    if not movies:
        return f"No movies to watch in genre '{genre}'"
    return random.choice(movies)

@app.route("/mark_watched", methods=["POST"])
def mark_watched():
    data = request.get_json()
    title = data.get("title")
    genre = data.get("genre")
    rating = data.get("rating")

    if not title or not genre or not rating:
        return "Missing 'title', 'genre', or 'rating'", 400

    r.srem(f"to_watch:{genre}", title)
    key = f"watched:{genre}:{title}"
    r.hset(key, mapping={"title": title, "genre": genre, "rating": rating})
    return f"✅ Marked '{title}' as watched with rating {rating}"

@app.route("/watched/<genre>", methods=["GET"])
def get_watched(genre):
    pattern = f"watched:{genre}:*"
    keys = r.keys(pattern)
    watched = [r.hgetall(k) for k in keys]
    return jsonify({genre: watched})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
