class SocialMediaApp:
    def __init__(self):
        self.followers = {}
    def add_follower(self, user, follower):
        if user not in self.followers:
            self.followers[user] = set()
        self.followers[user].add(follower)
    def get_followers(self, user):
        return self.followers.get(user, set())
app = SocialMediaApp()
app.add_follower("user1", "madina")
app.add_follower("user1", "Ngoga")
app.add_follower("user2", "Merci")
app.add_follower("user2", "Fanny")
app.add_follower("user3", "Super")
app.add_follower("user3", "Aline")
print(app.get_followers("user1"))
print(app.get_followers("user2"))
print(app.get_followers("user3"))