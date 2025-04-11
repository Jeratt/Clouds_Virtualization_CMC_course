from flask import Flask, request, jsonify
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis', password='', port=6379, decode_responses=True)

@app.route('/albums/<band>', methods=['GET'])
def get_albums(band):
    albums = redis_client.lrange(f'band:{band}', 0, -1)
    if not albums:
        return jsonify({'error': 'Band not found or no albums'}), 404
    return jsonify({'band': band, 'albums': albums}), 200

@app.route('/albums', methods=['POST'])
def add_album():
    data = request.json
    band = data.get('band')
    album = data.get('album')

    if not band or not album:
        return jsonify({'error': 'Band and album are required'}), 400

    key = f'band:{band}'
    redis_client.rpush(key, album)
    return jsonify({'message': f'Album "{album}" added to {band}'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)