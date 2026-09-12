from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
posts_db = []

@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    if not data or 'user_id' not in data or 'content' not in data:
        return jsonify({'error': 'Invalid request parameters'}), 400
    
    post = {
        'post_id': len(posts_db) + 1,
        'user_id': data['user_id'],
        'content': data['content'],
        'timestamp': datetime.datetime.now().isoformat(),
        'likes': 0
    }
    posts_db.append(post)
    return jsonify({'message': 'Post created successfully', 'post': post}), 201

@app.route('/api/feed', methods=['GET'])
def get_feed():
    return jsonify({'feed': posts_db, 'total': len(posts_db)}), 200

if __name__ == '__main__':
    app.run(debug=True)
