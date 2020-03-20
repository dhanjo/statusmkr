#!/usr/bin/env python
import requests
import os
import sys
from collections import namedtuple


try :
    print("""
    ____  _        _             __  __      _
    / ___|| |_ __ _| |_ _   _ ___|  \/  |_ __| | __
    \___ \| __/ _` | __| | | / __| |\/| | '__| |/ /
     ___) | || (_| | |_| |_| \__ \ |  | | |  |   <
    |____/ \__\__,_|\__|\__,_|___/_|  |_|_|  |_|\_\


    ## Coded by Dhananjay Garg | Insta - @dhananjaygarg_
    """)

    web_list = sys.argv[1]
    status_name = sys.argv[2]
    web_scan_list = 'cat ' + web_list + ' | httprobe > ' + status_name
    htrob = os.system(web_scan_list)
    WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
    names = ['foo', 'bar']


    def get_status(site):
        try:
            response = requests.head(site, timeout=5)
            status_code = response.status_code
            reason = response.reason
        except (requests.exceptions.ConnectionError,requests.exceptions.ReadTimeout):
            status_code = '000'
            reason = 'ConnectionError'
        website_status = WebsiteStatus(status_code, reason)
        return website_status

    with open(status_name) as f:
        sub = [line.rstrip('\n') for line in f]

    for si in sub:
        for name in names:
            site = str(si).format(name)
            website_status = get_status(site)
            print("{0:30} {1:10} {2:10}"
                .format(site, website_status.status_code, website_status.reason))
except (IndexError):
    print("""
    Usage :- python statusmrk.py <subdomain file> <output file>
        """)
