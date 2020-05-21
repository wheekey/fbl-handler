import re


class EmailExtractor():

    def extract_email(self, grep_content: str, message_id: str) -> str:
        groups = re.search(".*" + message_id + "\s=>\s(.+?)\sR=dnslookup.*", grep_content, flags=re.MULTILINE|re.UNICODE).groups()

        if groups is None:
            return ''

        return groups[0]
