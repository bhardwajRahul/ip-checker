from time import sleep

from checker import CheckerIP, docker_log


def main():

    checker = CheckerIP()

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
