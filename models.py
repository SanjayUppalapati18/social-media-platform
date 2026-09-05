class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

class Post:
    def __init__(self, post_id, author_id, content, timestamp):
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.timestamp = timestamp
