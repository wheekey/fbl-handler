import paramiko
from fbl_handler import SSHConnector
from dotenv import load_dotenv
import os
load_dotenv()


class SFTPManager():

    def __init__(self, sftp: paramiko.SFTPClient, ssh: paramiko.SSHClient):
        self.sftp = sftp
        self.ssh = ssh

    def grep_chunk_with_email_in_exim_log(self, exim_log_path: str, message_id: str):
        command = "cat " + exim_log_path + " | grep " + message_id
        ssh_stdin, ssh_stdout, ssh_stderr = self.ssh.exec_command(command)
        opt = ssh_stdout.readlines()
        opt = "".join(opt)
        return opt

    def get_file_content(self, abs_path_to_file: str):
        file_content = ''
        file_lines = self.sftp.open(abs_path_to_file).readlines()
        return file_content.join(file_lines)

    def get_last_file_contents_by_day(self, path_to_files: str):
        latest = 0
        latestfile = None
        file_contents = []
        seconds_in_a_day = 86400

        for fileattr in self.sftp.listdir_attr(path_to_files):
            if fileattr.st_mtime > latest:
                latest = fileattr.st_mtime
                latestfile = fileattr.filename

        if latestfile is None:
            return None

        latestfile_before_one_day = latest - seconds_in_a_day

        for fileattr in self.sftp.listdir_attr(path_to_files):
            if fileattr.st_mtime > latestfile_before_one_day:
                file_contents.append(self.get_file_content(path_to_files + "/" + fileattr.filename))

        return file_contents

    def get_filenames_in_dir(self, path_to_files: str) -> list:
        return self.sftp.listdir(path_to_files)
