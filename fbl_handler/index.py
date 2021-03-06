from fbl_handler.SFTPManager import SFTPManager
from fbl_handler.SSHConnector import SSHConnector
from fbl_handler.email_extractor import EmailExtractor
from fbl_handler.exim_logs_manager import EximLogsManager
from fbl_handler.message_id_extractor import MessageIdExtractor
from fbl_handler.subscriber_updater import SubscriberUpdater
from dotenv import load_dotenv
import traceback
import time
import os
import fbl_handler.wsgi
import logging
from fbl_handler.models import Message

load_dotenv()
logger = logging.getLogger('fbl_handler')

def is_fbl_mail_ru(mail_content: str) -> bool:
    return 'corp.mail.ru' in mail_content

def unsubscribe(message_id: str, email: str):
    logger.debug("Message %s ", [message_id])
    logger.debug("Email %s ", [email])
    if email != '' and not is_message_unsubscribed(email):
        subscriber_updater.unsubscribe_client(email)
        message = Message(message_id=message_id, email=email, is_unsubscribed=True)
        message.save()
        logger.debug("Message %s with email %s unsubscribedd", message_id, email)


def is_message_unsubscribed(email: str):
    try:
        Message.objects.get(email=email)
    except:
        logger.debug(email + " Еще не отписан")
        return False
    return True

def handle_as_yandex_fbl(email_content: str):
    message_id = message_id_extractor.extract_from_yandex_fbl(email_content)

    if message_id != '':
        grep_chunk = exim_logs_manager.get_log_chunk_with_email_by_message_id(message_id)
        if grep_chunk != '':
            email = email_extractor.extract_email(grep_chunk, message_id)
            unsubscribe(message_id, email)


def handle_as_mail_ru_fbl(email_content: str):
    message_id = 'mail.ru'
    email = email_extractor.mail_ru_extract_from_message_body(email_content)
    subscriber_updater.unsubscribe_client(email)
    unsubscribe(message_id, email)

logger.debug("FBL handler started.")

while True:
    logger.debug("коннект по ssh")
    try:
        ssh_connector = SSHConnector().create_connection()
        break
    except Exception as ex:
        time.sleep(5)


sftp_client = SSHConnector().get_sftp_client(ssh_connector)
sftp_manager = SFTPManager(sftp_client, ssh_connector)
email_extractor = EmailExtractor()
exim_logs_manager = EximLogsManager(sftp_manager)
message_id_extractor = MessageIdExtractor()
subscriber_updater = SubscriberUpdater()

email_contents = sftp_manager.get_last_file_contents_by_day(os.getenv('sftp_path_to_new_emails'))

for email_content in email_contents:
    try:
        if is_fbl_mail_ru(email_content):
            handle_as_mail_ru_fbl(email_content)
        else:
            handle_as_yandex_fbl(email_content)
    except Exception as ex:
        logger.debug(ex)
        logger.debug(traceback.print_exc())

