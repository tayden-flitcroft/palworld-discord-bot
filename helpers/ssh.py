import os
import paramiko

class SSH():
    def __init__(self):
        self.ip = os.environ['HOST_SERVER_IP']
        self.port = os.environ['HOST_SSH_PORT']
        self.username = os.environ['HOST_SSH_USERNAME']
        self.ssh_key_file_path = 'docs/ssh_key'

    def send_command(self, command) -> str:
        key = paramiko.RSAKey.from_private_key_file(self.ssh_key_file_path)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(self.ip, self.port, username=self.username, pkey=key)

        _ssh_stdin, ssh_stdout, _ssh_stderr = ssh.exec_command(command)
        result = ssh_stdout.read().decode('utf-8').strip()

        return result
