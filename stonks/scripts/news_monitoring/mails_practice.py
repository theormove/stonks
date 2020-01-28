import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create the base text message.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Ayons asperges pour le déjeuner"
msg['From'] = "2r.ivanets@gmail.com"
msg['To'] = "2r.ivanets@gmail.com"

html = """\
<html>
  <head></head>
  <body>
    <p>Salut!</p>
    <p>Cela ressemble à un excellent
        <a href="http://www.yummly.com/recipe/Roasted-Asparagus-Epicurious-203718">
            recipie
        </a> déjeuner.
    </p>
    <img src="cid:{asparagus_cid}" />
  </body>
</html>
"""

part1 = MIMEText(html, 'html')

msg.attach(part1)

s = smtplib.SMTP_SSL("smtp.gmail.com")
s.login("2r.ivanets@gmail.com", "r0man2001")
s.send_message(msg)