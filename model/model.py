from PyQt5.QtCore import QObject, pyqtSignal

class Model(QObject):
    def __init__(self):
        super().__init__()
        self.__username = ""
        self.__password = ""

    def set_username(self, username):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def get_credentials(self):
        self.__password = "pswd"