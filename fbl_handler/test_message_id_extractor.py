from unittest import TestCase

from fbl_handler.message_id_extractor import MessageIdExtractor


class TestMessageIdExtractor(TestCase):
    def setUp(self):
        self.message_id_extractor = MessageIdExtractor()

    def test_extract_from_yandex_fbl(self):
        with open('files/yandex_fbl.txt', 'r') as file:
            file_content = file.read()
        self.assertEqual(self.message_id_extractor.extract_from_yandex_fbl(file_content), '1jb6B3-0004MN-Dq')
