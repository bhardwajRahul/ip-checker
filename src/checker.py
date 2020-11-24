import os
import smtplib

from datetime import datetime

from email.message import EmailMessage

import requests

def docker_log(msg, lvl='INFO'):
    '''
    Simple function to log to stdout.

    Args:
        - msg (str): message to be logged
        - lvl (str, optional): level of logged message
    '''
    print(f'{datetime.now()}; {lvl.upper()}; {msg}')

class CheckerIP():
    '''
    Class that Checks IP of current device. Methods include:
        - notificating user
        - saving current ip to .txt file
        - reading last knows ip to .txt file

    Args:
        None.

    Attributes:
        ip (str): current IPv4 of device
        sender_email (str): E-mail used to send out notifications via email
        sender_email_pass (str): sender_email password
        telegram_bot_token (str): token of the telegram bot that will be used to
            send out notifications via telegram
        alert_list (disct): dictionary containing 2 lists, 'mail' and 'telegram'.
            Both are lists of chat_ids/mails to send out notifications to.
    '''

    def __init__(self):
        self.ip = self.get_ip()
        self.sender_email = os.environ.get('EMAIL_HOST_USER')
        self.sender_email_pass = os.environ.get('EMAIL_HOST_PASSWORD')
        self.telegram_bot_token = os.environ.get('TELEGRAM_BOT_KEY')
        self.alert_list = {
            'mail': os.environ.get('MAIL_LIST').split(','),
            'telegram': os.environ.get('TELEGRAM_CHAT_LIST').split(','),
        }

    def save_ip(self):
        '''
        Writes the last known IP to the `./last_ip.txt` file.

        Args:
            None.

        Returns:
            None.
        '''
        with open('./last_ip.txt', 'w') as file:
            file.write(f'{self.ip}')

    def read_ip(self):
        '''
        Reads the last known IP from the `./last_ip.txt` file.

        Args:
            None.

        Returns:
            None.
        '''
        with open('./last_ip.txt', 'r') as file:
            return file.read()


    def notify(self):
        '''
        Sends out notifications to configured methods.

        Args:
            None.

        Returns:
            None.
        '''

        for mail in self.alert_list['mail']:
            self._mail(mail)

        for chat in self.alert_list['telegram']:
            self._telegram(chat)

    def _mail(self, to_mail):
        '''
        Sends out an email warning about IP change.

        Args:
            None.

        Returns:
            None.
        '''
        smtp_server = 'smtp.gmail.com'
        port = 465

        msg = EmailMessage()
        msg['Subject'] = 'IP Change of Pi-VPN'
        msg['From'] = self.sender_email
        msg['To'] = to_mail
        msg.set_content(f'The IP of your Pi-VPN has changed, new IP:\n{self.ip}\n\nWith love,\nRaspberry-Pi.')

        with smtplib.SMTP_SSL(smtp_server, port) as smtp:
            smtp.login(self.sender_email, self.sender_email_pass)
            smtp.send_message(msg)


    def _telegram(self, chat_id):
        '''
        Sends out a telegram warning about IP change.

        Args:
            None.

        Returns:
            None.
        '''

        text = f'Pi-VPN IP Change:\n{self.ip}'
        url = f'https://api.telegram.org/bot{self.telegram_bot_token}/sendMessage'
        url += f'?chat_id={chat_id}&text={text}'

        r = requests.get(url)

        if r.status_code != 200:
            docker_log(lvl='ERROR', msg=f'Error when trying to send Telegam Message,\
            check your TELEGRAM_CHAT_LIST and TELEGRAM_BOT_KEY ENV variables.\
            CHAT_NUM={chat_id}')


    @staticmethod
    def get_ip():
        '''
        Gets the public IP Address of current device.

        Args:
            None.

        Returns:
            ip (str): public IP of device.
        '''

        return requests.get('https://checkip.amazonaws.com').text.strip()
