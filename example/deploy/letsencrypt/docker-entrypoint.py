#!/bin/python

import time
import os
print(os.popen("uptime").read())
PATH = '/apps'
LETSENCRYPT_LIVE = '/etc/letsencrypt/live/'

while True:
    for directory in os.listdir(PATH):
        print directory
        if directory is 'balancer':
            continue

        domains = []
        try:
            with open(os.path.join(PATH,directory,'acme','request-domains.txt')) as fileDomains:
                for line in fileDomains:
                    domain = line.strip()
                    if len(domain) > 4 and not os.path.exists(os.path.join(LETSENCRYPT_LIVE,domain)):
                        domains.append(line.strip())

            if len(domains) is 0:
                continue

            args = [
                'letsencrypt','certonly',
                '--agree-tos',
                '-n',
                '-t',
                '--webroot',
                '-m','mikeifomin@gmail.com',
                '-w','/acme'
                ]
            for domain in domains:
                args.append("-d")
                args.append(domain)

            res = os.popen(" ".join(args)).read()
            print(res)
        except IOError:
            pass
        # print(" ".join(args))


    time.sleep(3600*24*40)
    res = os.popen("letsencrypt renew").read()
    print(res)
    print(os.popen("uptime").read())
