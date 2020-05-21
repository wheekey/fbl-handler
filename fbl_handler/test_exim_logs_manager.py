from unittest import TestCase

from fbl_handler.SFTPManager import SFTPManager
from fbl_handler.SSHConnector import SSHConnector
from fbl_handler.exim_logs_manager import EximLogsManager


class TestEximLogsManager(TestCase):
    
    def setUp(self):
        self.ssh_connector = SSHConnector().create_connection()
        self.sftp_client = SSHConnector().get_sftp_client()
        self.sftp_manager = SFTPManager(self.sftp_client, self.ssh_connector)
        self.exim_logs_manager = EximLogsManager(self.sftp_manager)

    def tearDown(self):
        self.ssh_connector.close()


class TestInit(TestEximLogsManager):
    def test_logs_paths_with_full_path(self):
        filenames = self.exim_logs_manager.get_logs_abs_paths()
        self.assertTrue(filenames[0].find('/') != -1)
