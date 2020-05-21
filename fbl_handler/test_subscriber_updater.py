from unittest import TestCase

from fbl_handler.subscriber_updater import SubscriberUpdater


class TestSubscriberUpdater(TestCase):
    def setUp(self):
        self.subscriberUpdater = SubscriberUpdater()


class TestInit(TestSubscriberUpdater):

    def test_unsubscribe_client(self):
        self.subscriberUpdater.unsubscribe_client('dmitr-shust@yandex.ru')

