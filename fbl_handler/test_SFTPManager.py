from unittest import TestCase

from fbl_handler.SFTPManager import SFTPManager
from fbl_handler.SSHConnector import SSHConnector

from dotenv import load_dotenv
import os
load_dotenv()


class TestSftpManager(TestCase):
    def setUp(self):
        self.ssh_connector = SSHConnector().create_connection()
        self.sftp_client = SSHConnector().get_sftp_client()
        self.sftp_manager = SFTPManager(self.sftp_client, self.ssh_connector)

    def tearDown(self):
        self.ssh_connector.close()


class TestInit(TestSftpManager):
    def test_get_file_content(self):
        self.assertNotEqual('', self.sftp_manager.get_file_content('/home/admin/mail/togas-shop.ru/abuse/new/1589877155.H352051P31483.CentOS-65-64-minimal'))

    def test_get_last_files_by_day(self):
        self.assertIsNotNone(self.sftp_manager.get_last_file_contents_by_day(os.getenv('sftp_path_to_new_emails')))

    def test_get_filenames_in_dir(self):
        self.assertTrue(len(self.sftp_manager.get_filenames_in_dir(os.getenv('sftp_path_to_exim_logs'))) != 0)

    def test_grep_id_in_exim_log(self):
        self.sftp_manager.grep_chunk_with_email_in_exim_log(os.getenv('sftp_path_to_exim_logs') + "/main.log", '1jb6B3-0004MN-Dq')

    def test_from_exim_log_returns_empty_string_if_not_found_message_id(self):
        self.assertEqual('', self.sftp_manager.grep_chunk_with_email_in_exim_log(os.getenv('sftp_path_to_exim_logs') + "/main.log", '123456789abcd'))

