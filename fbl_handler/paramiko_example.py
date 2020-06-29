import paramiko
from dotenv import load_dotenv
import os
load_dotenv()

sftpURL=os.getenv('sftp_url')
sftpUser=os.getenv('sftp_user')
sftpPass=os.getenv('sftp_pass')


ssh = paramiko.SSHClient()
# automatically add keys without requiring human intervention
ssh.set_missing_host_key_policy( paramiko.AutoAddPolicy())

ssh.connect(sftpURL, username=sftpUser, password=sftpPass)

ftp = ssh.open_sftp()
files = ftp.listdir('/var/tmp/')
print(files)