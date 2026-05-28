#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "31685568"))
    API_HASH = os.environ.get("API_HASH", "436f53caee1dcae5eefcdf373716fccb")
    AUTH_USERS = os.environ.get("AUTH_USERS", "2083529027")
