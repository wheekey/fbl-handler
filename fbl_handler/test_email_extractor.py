from unittest import TestCase

from fbl_handler.email_extractor import EmailExtractor

class TestEmailExtractor(TestCase):
    def setUp(self):
        self.message_id_extractor = EmailExtractor()

    def test_mail_ru_extract_from_message_body(self):
        with open('files/mail_fbl.txt', 'r') as file:
            file_content = file.read()
        self.assertEqual(self.message_id_extractor.mail_ru_extract_from_message_body(file_content), 'sokolusha80@mail.ru')
