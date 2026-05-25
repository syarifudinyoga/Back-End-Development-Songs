from flask import Flask, jsonify, request

app = Flask(__name__)

songs = [
    {
        "id": 1,
        "title": "Imagine",
        "artist": "John Lennon"
    }
]

@app.route("/songs/<int:song_id>", methods=["PUT"])
def update_song(song_id):
    song = next((s for s in songs if s["id"] == song_id), None)

    if not song:
        return jsonify({
            "message": "Song not found"
        }), 404

    data = request.get_json()

    song["title"] = data.get("title", song["title"])
    song["artist"] = data.get("artist", song["artist"])

    return jsonify({
        "message": "Song updated successfully",
        "song": song
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
