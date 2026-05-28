#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7864597080:AAH7YFZM0ps4JGk6997RPZ-Xv-Ar-6bFUxA")
    API_ID = int(os.environ.get("API_ID", "21567814"))
    API_HASH = os.environ.get("API_HASH", "cd7dc5431d449fd795683c550d7bfb7e")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6126688051")
