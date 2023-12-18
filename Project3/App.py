from flask import Flask, request, jsonify
from datetime import datetime
from secrets import token_urlsafe

app = Flask(__name__)

posts = {}
replies = {}
key_store = {}
users = {}
user_profiles = {}
user_tokens = {}
admin_users = set()  # Set to store admin users

def generate_post_id():
    return max(posts.keys(), default=0) + 1

def generate_secure_key():
    return token_urlsafe(16)

def generate_user_token():
    return token_urlsafe(32)

@app.route('/post', methods=['POST'])
def create_post():
    data = request.json
    if not data or 'msg' not in data:
        return jsonify({'err': 'Bad request, missing msg field'}), 400

    post_id = generate_post_id()
    key = generate_secure_key()
    timestamp = datetime.utcnow().isoformat()
    parent_id = data.get('parent_id')  # For threaded discussions

    new_post = {
        'id': post_id, 
        'msg': data['msg'], 
        'timestamp': timestamp,
        'parent_id': parent_id,
        'user': data.get('user'),  # Linking post to a user
        'replies': []
    }
    posts[post_id] = new_post

    if parent_id and parent_id in posts:
        replies.setdefault(parent_id, []).append(post_id)
        posts[parent_id]['replies'].append(post_id)

    key_store[post_id] = key

    return jsonify({'id': post_id, 'key': key, 'timestamp': timestamp}), 201

@app.route('/search', methods=['GET'])
def search_posts():
    query = request.args.get('query', '')
    search_results = [post for post in posts.values() if query.lower() in post['msg'].lower()]
    return jsonify(search_results), 200

@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'err': 'Missing username or password'}), 400

    username = data['username']
    if username in users:
        return jsonify({'err': 'Username already taken'}), 400

    users[username] = data['password']
    user_profiles[username] = {
        'bio': data.get('bio'),
        'profile_pic': data.get('profile_pic')
    }

    if data.get('is_admin'):
        admin_users.add(username)

    return jsonify({'msg': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'err': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    if username not in users or users[username] != password:
        return jsonify({'err': 'Invalid username or password'}), 403

    token = generate_user_token()
    user_tokens[username] = token
    return jsonify({'token': token}), 200

@app.route('/user/<username>', methods=['GET'])
def get_user_profile(username):
    profile = user_profiles.get(username)
    if not profile:
        return jsonify({'err': 'User not found'}), 404
    return jsonify(profile), 200

@app.route('/admin/posts', methods=['GET'])
def list_all_posts():
    token = request.args.get('token')
    if token not in user_tokens.values():
        return jsonify({'err': 'Unauthorized'}), 403
    return jsonify(list(posts.values())), 200

@app.route('/analytics/dashboard', methods=['GET'])
def analytics_dashboard():
    token = request.args.get('token')
    if token not in user_tokens.values():
        return jsonify({'err': 'Unauthorized'}), 403

    dashboard_data = {
        'total_posts': len(posts),
        'total_users': len(users)
    }
    return jsonify(dashboard_data), 200

if __name__ == '__main__':
    app.run(debug=True)
