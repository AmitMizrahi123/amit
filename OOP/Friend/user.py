from OOP_Friend.post import Post


class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.posts = []

    def add_post(self, text, user):
        self.posts.append(Post(text, user))

    def add_friend(self, user):
        self.friends.append(User(user))


if __name__ == '__main__':
    amit = User("amit")
    amit.add_post("hello", "amit")
    amit.add_post("world", "amit")
    [print(post.text) for post in amit.posts]