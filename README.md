<!-- PROJECT LOGO -->

<br />
<p align="center">
  <!-- <a href="LOGO.png">
    <img src="LOGO.png" alt="Logo" width="230" height="auto">
  </a> -->

  <h3 align="center">Home IP Checker</h3>

  <p align="center">
    A simple script to notify you when your home ip changes.
    <br />
    <a href="https://github.com/LombardiDaniel/ip-checker"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LombardiDaniel/ip-checker/issues">Report Bug</a>
    ·
    <a href="https://github.com/LombardiDaniel/ip-checker/issues">Request Feature</a>
  </p>
</p>

## Table of Contents

-   [About the Project](#about-the-project)
-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Installation](#installation)
-   [Usage](#usage)
-   [License](#license)

### About the Project

The idea behind this repo is a simple way to guarantee that you'll always able to connect to you [PiVPN](https://www.pivpn.io) even if your internet provider changes your public IP (made in case you wish to not use a static ip service). By sending a notification via Telegram whenever the IP of you Raspberry Pi changes, you'll never be left out of your home network!

The system is a very simple python script that uses [amazon AWS](https://checkip.amazonaws.com) to get the current IPv4 Address of the device (must be running in the same machine as the VPN).

### Getting Started

#### Prerequisites

To maximize compatbility, you will only need [docker](https://www.docker.com/) and docker-compose to be installed on your computer. But if you wish to not run it as a container, feel free to check [requirements.txt](requirements.txt) file and run it as a separate service, just `cd` into the [src](/src) folder and run `python3 run.py`. Make sure to edit the `run.py` file and set your own variables.

For the notifications, you will need a configured Telegram Bot. For the Telegram Bot, you'll need 2 things: the Chat ID of the people that will receive the notification, as well as the bot ID. You can learn about them [here](https://core.telegram.org/bots).

#### Instalation

Since the script is containerized, just run `git pull https://github.com/LombardiDaniel/ip-checker`, `cd ip-checker`. Create a `.env` file with the variables described below.

### Usage

The only configuration needed is to set the environment variables in the `.env` file. Configure your Telegram key in the `.env` file (separate multiple addresses by using `,`) and run `docker-compose up -d`. It logs to `stdout`, so you can easily check the logs via [portainer](https://www.portainer.io).

|    Variable Name   | Meaning                                    | Separator |
| :----------------: | ------------------------------------------ | :-------: |
| TELEGRAM_CHAT_LIST | List of chat keys to send notifications to |    `,`    |
|  TELEGRAM_BOT_KEY  | Bot API  Keys to send notifications to     |     -     |

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
