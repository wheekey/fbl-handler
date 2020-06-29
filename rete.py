import re

text = """Return-path: <fbl@bounce.mailstream.senderscore.net>
Envelope-to: abuse@togas-shop.ru
Delivery-date: Mon, 18 May 2020 10:53:11 +0200
Received: from mrd.us-east-1b.returnpath.net ([52.20.42.191])
        by CentOS-65-64-minimal with esmtps (TLSv1.2:ECDHE-RSA-AES128-GCM-SHA256:128)
        (Exim 4.92)
        (envelope-from <fbl@bounce.mailstream.senderscore.net>)
        id 1jabWJ-0002z9-8p
        for abuse@togas-shop.ru; Mon, 18 May 2020 10:53:11 +0200
Received: (Haraka outbound); Mon, 18 May 2020 08:53:05 +0000
Received: from localhost ([10.252.36.161])
        by mrd.us-east-1b.returnpath.net (Haraka/2.8.21) with ESMTP id BCDD27CF-8E40-49D3-88E2-60832ACC3853.1
        envelope-from <fbl@bounce.mailstream.senderscore.net>;
        Mon, 18 May 2020 08:53:05 +0000
From: Yandex FBL Service <feedbackloop@yandexfbl.senderscore.net>
Date: Mon, 18 May 2020 08:53:05 +0000
Mime-Version: 1.0
X-Rp-Fbl: type=arf; subscriptionID=96781
Content-Type: multipart/report; report-type=feedback-report;
 boundary=51dd9d1916ed201fb9b522f92e7f700c99a25c685db55dcef77566fbf626
Message-Id: <01E8KFS3VKFKCRVBXZTHVRETJB.fbl@bounce.mailstream.senderscore.net>
To: abuse@togas-shop.ru
Subject: Yandex Abuse Report
DKIM-Signature: v=1;a=rsa-sha256;bh=MedelWF7/z2GlBt/T+9meAHD+JsOtjqWgJ+V+FgYV1Q=;c=relaxed/simple;d=senderscore.net;h=from:to:subject;s=081107;b=qLDL/f4yQo+Jpj1WcO5yQj+6sMqzJGx2b09ZI3NStPD7iNRKPThoDyu1bokPsyWxVZxwnPOpypABbZR9i0mk+scJ4cBxxQ5e7pbEk5giugMQQidQ26xlViyZVHe3pWPSgfQAmnY7RmtcGvzVET2q6rjeXhnUF5bd2lsbaVg3xcc=

--51dd9d1916ed201fb9b522f92e7f700c99a25c685db55dcef77566fbf626
Content-Transfer-Encoding: quoted-printable
Content-Type: text/plain; charset=UTF-8

This is a Yandex Abuse Report for an email message received from domain tog=
as-shop.ru, IP 78.46.251.116, on Sat, 16 May 2020 03:01:44 +0000.

--51dd9d1916ed201fb9b522f92e7f700c99a25c685db55dcef77566fbf626
Content-Disposition: inline
Content-Transfer-Encoding: 8bit
Content-Type: message/feedback-report

Original-Rcpt-To: ca2b45ef141c63af66829a2f346c832b@email.xxx
Source-Ip: 78.46.251.116
Feedback-Type: abuse
User-Agent: ReturnPathFBL/2.0
Original-Mail-From: bounce@togas-shop.ru
Reported-Domain: togas-shop.ru
Source: Yandex
Abuse-Type: complaint
Subscription-Link: https://fbl.returnpath.net/manage/subscriptions/96781
Version: 1
Arrival-Date: Sat, 16 May 2020 03:01:44 +0000

--51dd9d1916ed201fb9b522f92e7f700c99a25c685db55dcef77566fbf626
Content-Disposition: inline
Content-Transfer-Encoding: 8bit
Content-Type: message/rfc822

Received: from <ca2b45ef141c63af66829a2f346c832b> (localhost [127.0.0.1])
 by <ca2b45ef141c63af66829a2f346c832b> with LMTP id 7l0kOqqPPF-6lnoixuu
 for <<ca2b45ef141c63af66829a2f346c832b@email.xxx>>; Sat, 16 May 2020 21:49:55 +0300
Received: from mail.togas-shop.ru (mail.togas-shop.ru [78.46.251.116])
 by <ca2b45ef141c63af66829a2f346c832b> (mxfront/Yandex) with ESMTPS id sJEvfxvmTG-ntGSb5v1;
 Sat, 16 May 2020 21:49:55 +0300
 (using TLSv1.2 with cipher ECDHE-RSA-AES128-GCM-SHA256 (128/128 bits))
 (Client certificate not present)
Return-Path: bounce@togas-shop.ru
Authentication-Results: <ca2b45ef141c63af66829a2f346c832b>; spf=pass (<ca2b45ef141c63af66829a2f346c832b>: domain of togas-shop.ru
 designates 78.46.251.116 as permitted sender, rule=[a])
 smtp.mail=bounce@togas-shop.ru; dkim=pass header.i=@togas-shop.ru
Received: from mail.togas-shop.ru ([78.46.251.116] helo=togas-shop.ru)
 by CentOS-65-64-minimal with esmtpa (Exim 4.92)
 (envelope-from <bounce@togas-shop.ru>) id 1ja1sg-0005gL-HH
 for <ca2b45ef141c63af66829a2f346c832b@email.xxx>; Sat, 16 May 2020 20:49:54 +0200
To: <ca2b45ef141c63af66829a2f346c832b@email.xxx>
Subject: =?utf-8?q?C=D0=B4=D0=B5=D0=BB=D0=B0=D0=B9=D1=82=D0=B5_=D1=81=D0=B2=D0=BE?= =?utf-8?q?=D1=8E_=D1=81=D0=BF=D0=B0=D0=BB=D1=8C=D0=BD=D1=8E_=D1=83=D1=8E?= =?utf-8?q?=D1=82=D0=BD=D0=B5=D0=B5_=D0=B2=D1=81=D0=B5=D0=B3=D0=BE_=D0=B7?= =?utf-8?q?=D0=B0_=D0=BE=D0=B4=D0=B8=D0=BD_=D0=B4=D0=B5=D0=BD=D1=8C!_?= =?utf-8?q?=D0=A0=D0=B0=D1=81=D0=BF=D1=80=D0=BE=D0=B4=D0=B0=D0=B6=D0=B0_?= =?utf-8?q?=D0=B1=D1=80=D0=B5=D0=BD=D0=B4=D0=B0_Cleo!_=D0=A1=D0=BA=D0=B0?= =?utf-8?q?=D0=B7=D0=BE=D1=87=D0=BD=D1=8B=D0=B5_=D1=86=D0=B5=D0=BD=D1=8B_?= =?utf-8?q?=E2=80=93_=D0=B2=D1=81=D0=B5=D0=B3=D0=BE_=D0=BE=D1=82_230_?= =?utf-8?q?=D1=80=D1=83=D0=B1!?=
Date: Sat, 16 May 2020 03:01:44 +0000
From: "=?UTF-8?B?0JTQvtC80LDRiNC90LjQuSDQotC10LrRgdGC0LjQu9GM?="
 <info@togas-shop.ru>
Reply-To: info@togas-shop.ru
MIME-Version: 1.0
Content-Type: multipart/alternative; charset="UTF-8";
 boundary="b1_fb519b0a3730bc85cdee82d5f20c2150"
Content-Transfer-Encoding: 8bit



--51dd9d1916ed201fb9b522f92e7f700c99a25c685db55dcef77566fbf626--
"""

z = re.search(".*bounce@togas-shop\.ru>\\)\sid\s(.+?)\s.*", text, flags=re.MULTILINE|re.UNICODE)

print(z.groups())
