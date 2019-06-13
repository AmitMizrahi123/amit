from OOP_Friend.comment import Comment


class Post:
    def __init__(self, post_text, user):
        self.text = post_text
        self.user = user
        self.comments = []

    def add_comment(self, text, user):
        self.comments.append(Comment(text, user))
