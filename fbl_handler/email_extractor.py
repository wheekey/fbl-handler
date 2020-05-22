import re


class EmailExtractor():

    def extract_email(self, grep_content: str, message_id: str) -> str:
        groups = re.search(".*" + message_id + "\s=>\s(.+?)\sR=dnslookup.*", grep_content, flags=re.MULTILINE|re.UNICODE).groups()

        if groups is None:
            return ''

        return groups[0]

    def mail_ru_extract_from_message_body(self, message_body: str):
        matches = re.findall("\sTo:\s(.+?)\s", message_body)

        if matches is None:
            return ''

        return matches[len(matches)-1]