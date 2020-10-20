import re
import os
from dotenv import load_dotenv

load_dotenv()

class MessageIdExtractor():

    def extract_from_yandex_fbl(self, message_content: str) -> str:
        print(1234)
        search = re.search(".*" + os.getenv('fbl_pattern_yandex') + "\.ru>\\)\sid\s(.+?)\s.*", message_content,
                           flags=re.MULTILINE | re.UNICODE)

        if search is None:
            return ''

        return search.groups()[0]


