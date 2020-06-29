import re

text = """2020-05-19 19:37:17 1jb6B3-0004MN-Dq <= bounce@togas-shop.ru H=mail.togas-shop.ru (togas-shop.ru) [78.46.251.116] P=esmtpa A=dovecot_login:news@togas-shop.ru S=21082 id=01c742771ba232a0ec34684836289d15@togas-shop.ru
2020-05-19 19:37:17 1jb6B3-0004MN-Dq [93.158.134.89] SSL verify error: depth=2 error=unable to get local issuer certificate cert=/C=PL/O=Unizeto Technologies S.A./OU=Certum Certification Authority/CN=Certum Trusted Network CA
2020-05-19 19:37:17 1jb6B3-0004MN-Dq [93.158.134.89] SSL verify error: depth=2 error=certificate not trusted cert=/C=PL/O=Unizeto Technologies S.A./OU=Certum Certification Authority/CN=Certum Trusted Network CA
2020-05-19 19:37:18 1jb6B3-0004MN-Dq => klimen-lyudmila@yandex.ru R=dnslookup T=remote_smtp H=mx.yandex.ru [93.158.134.89] X=TLSv1.2:ECDHE-RSA-AES128-GCM-SHA256:128 CV=no C="250 2.0.0 Ok: queued on mxfront7o.mail.yandex.net as 1589909839-bA0qK0Zi51-bIQuI0q9"
2020-05-19 19:37:18 1jb6B3-0004MN-Dq Completed
"""
mes = '1jb6B3-0004MN-Dq'

z = re.search(".*" + mes + "\s=>\s(.+?)\sR=dnslookup.*", text, flags=re.MULTILINE|re.UNICODE)

print(z.groups())
