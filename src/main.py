from os import listdir
import smtplib
import imghdr
from email.message import EmailMessage

def send():
    # EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    # EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    EMAIL_ADDRESS = 'Sergej_kajnov@mail.ru'
    # EMAIL_ADDRESS = 'blooddesertparteim@gmail.com'
    EMAIL_PASSWORD = '2599360977Aa'
    # EMAIL_PASSWORD = 'mditoblruuvjatny'

    msg = EmailMessage()
    msg['Subject'] = 'Test mail'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = 'igc16865@eoopy.com'
    msg.set_content('This is the body of test message')

    with open('maxresdefault.jpg', 'rb') as img:
        file_data = img.read()
        file_type = imghdr.what(img.name)
        file_name = img.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    with smtplib.SMTP_SSL('smtp.mail.ru', 465) as smtp:
        # smtp.ehlo()
        # smtp.starttls()
        # smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        # smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
        smtp.send_message(msg)


def get_USR_files():
    for i in listdir('E:\consultant\RECEIVE'):
        if i.split('.')[1] == 'USR':
            print(i)

get_USR_files()