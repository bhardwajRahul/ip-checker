from datetime import datetime

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
        telegram_bot_token (str): token of the telegram bot that will be used to
            send out notifications via telegram
        telegram_list (lst of str): list of chat_ids to notify via telegram.

    Attributes:
        ip (str): current IPv4 of device
        telegram_bot_token (str): token of the telegram bot that will be used to
            send out notifications via telegram
        alert_list (disct): dictionary containing a list (key='telegram') of
            chat_ids to send out notifications to.
    '''

    def __init__(self, telegam_bot_token, telegram_list):
        self.ip = self.get_ip()
        self.telegram_bot_token = telegam_bot_token
        self.alert_list = {
            'telegram': telegram_list,
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

    @staticmethod
    def read_ip():
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

        for chat in self.alert_list['telegram']:
            self._telegram(chat)

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
            msg = ''
            msg += 'Error when trying to send Telegam Message, '
            msg += 'check your TELEGRAM_CHAT_LIST and TELEGRAM_BOT_KEY ENV variables. '
            msg += f'CHAT_ID={chat_id}'
            docker_log(lvl='ERROR', msg=msg)


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
