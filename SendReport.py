import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

PATH_TO_SCREENS = './'


def find_screenshots():
    files = os.listdir(PATH_TO_SCREENS)
    return filter(lambda x: x.endswith('.png'), files)


def delete_temp_files(self):
    png_files = find_screenshots()
    for file in png_files:
        os.remove(PATH_TO_SCREENS + file)


class Report:
    def __init__(self):
        self.addr_from = "test@gmail.com"
        self.addr_to = "test_to@mail.ru"
        self.password = "test_password"

    def make_message(self):
        msg = MIMEMultipart()
        msg['From'] = self.addr_from
        msg['To'] = self.addr_to
        msg['Subject'] = 'Скриншоты'

        png_files = find_screenshots()
        if not png_files:
            for file in png_files:
                fp = open(file, 'rb')
                img = MIMEImage(fp.read())
                fp.close()
                msg.attach(img)
            return msg

    def send(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.addr_from, self.password)
        server.send_message(self.make_message())
        server.quit()
        delete_temp_files()


