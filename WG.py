class WordlistGenerator():
    def __init__(self, leght, words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.words = words
        self.leght = leght
        self.password = list("0" * self.leght)
        self.len_passord = len(self.words) ** self.leght
        self.i = self.leght - 1
        self.Programm = True
    def next(self):
        while self.i >= 0:
            if self.i != 0:
                if int(self.password[self.i]) >= len(self.words):
                    self.password[self.i-1] = int(self.password[self.i-1]) + 1
                    self.password[self.i] = 0
            self.i -= 1
            if self.password[0] == len(self.words):
                self.Programm = False
            if self.Programm != False:
                temp = ""
                for self.i in range(self.leght):
                    temp += self.words[int(self.password[self.i])]
                self.password[self.leght - 1] = int(self.password[self.leght - 1]) + 1
                return temp
