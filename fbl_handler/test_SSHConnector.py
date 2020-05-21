from unittest import TestCase

import paramiko

from fbl_handler.SSHConnector import SSHConnector


class TestSSHConnector(TestCase):
    def setUp(self):
        self.sshConnector = SSHConnector()


class TestInit(TestSSHConnector):
    def test_create_connection(self):
        self.assertIsInstance(self.sshConnector.create_connection(), paramiko.SSHClient)

    def test_get_sftp_client(self):
        self.assertIsInstance(self.sshConnector.get_sftp_client(), paramiko.SFTPClient)
