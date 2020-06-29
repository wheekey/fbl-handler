import re


class MessageIdExtractor():

    def extract_from_yandex_fbl(self, message_content: str) -> str:
        groups = re.search(".*bounce@togas-shop\.ru>\\)\sid\s(.+?)\s.*", message_content,
                           flags=re.MULTILINE | re.UNICODE).groups()

        if groups is None:
            return ''

        return groups[0]
