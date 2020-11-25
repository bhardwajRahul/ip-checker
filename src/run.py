from time import sleep

from checker import CheckerIP, docker_log


def main():

    sender_email = os.environ.get('EMAIL_HOST_USER')
    sender_email_pass = os.environ.get('EMAIL_HOST_PASSWORD')
    telegram_bot_token = os.environ.get('TELEGRAM_BOT_KEY')
    mail_list = os.environ.get('MAIL_LIST').split(',')
    telegram_list = os.environ.get('TELEGRAM_CHAT_LIST').split(',')

    checker = CheckerIP(sender_email, sender_email_pass, telegram_bot_token, mail_list, telegram_list)

    old_ip = checker.read_ip()
    new_ip = checker.get_ip()

    while True:

        if new_ip != old_ip:
            docker_log('IP CHANGE', lvl='WARNING')
            checker.save_ip()
            checker.notify()

        old_ip = new_ip
        new_ip = checker.get_ip()

        docker_log('ITERATED')

        sleep(60)


if __name__ == '__main__':
    main()
