import paramiko
import os
from dotenv import load_dotenv

load_dotenv()


class SSHConnector():

    def create_connection(self) -> paramiko.SSHClient:
        sftpURL = os.getenv('sftp_url')
        sftpUser = os.getenv('sftp_user')
        sftpPass = os.getenv('sftp_pass')

        ssh = paramiko.SSHClient()
        # automatically add keys without requiring human intervention
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        ssh.connect(sftpURL, username=sftpUser, password=sftpPass, banner_timeout=200)

        return ssh

    def get_sftp_client(self) -> paramiko.SFTPClient:
        ssh_connection = self.create_connection()
        return ssh_connection.open_sftp()
