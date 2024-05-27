
class User():
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video():
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube():
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        

    #def log_in(self, login, password):



u1 = User('Ps1nu5', '123123', 24)
users_list = [u1]
videos_list = []

ut = UrTube(users_list, videos_list, u1)
ut.log_in()

print(u1.check_password('1231231'))
