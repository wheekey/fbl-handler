from fbl_handler.SFTPManager import SFTPManager
from dotenv import load_dotenv
import os

load_dotenv()


class EximLogsManager():

    def __init__(self, sftp_manager: SFTPManager):
        self.sftp_manager = sftp_manager

    def get_logs_abs_paths(self) -> list:
        path_to_logs = os.getenv('sftp_path_to_exim_logs')
        filenames = self.sftp_manager.get_filenames_in_dir(path_to_logs)

        return [path_to_logs + "/" + x for x in filenames]

    def get_log_chunk_with_email_by_message_id(self, message_id: str) -> str:
        filenames = self.get_logs_abs_paths()

        for filename in filenames:
            grep = self.sftp_manager.grep_chunk_with_email_in_exim_log(filename, message_id)
            if grep != '':
                return grep

        return ''
