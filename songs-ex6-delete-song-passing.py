from flask import Flask, jsonify

app = Flask(__name__)

songs = [
    {
        "id": 1,
        "title": "Imagine",
        "artist": "John Lennon"
    }
]

@app.route("/songs/<int:song_id>", methods=["DELETE"])
def delete_song(song_id):
    global songs

    song = next((s for s in songs if s["id"] == song_id), None)

    if not song:
        return jsonify({
            "message": "Song not found"
        }), 404

    songs = [s for s in songs if s["id"] != song_id]

    return jsonify({
        "message": "Song deleted successfully"
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
