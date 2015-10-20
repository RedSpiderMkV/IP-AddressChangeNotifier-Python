#!usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:51:17 2014

@author: RedSpiderMkV
"""

import datetime
import urllib2
import os
import json

class IpRetriever:
    url = r'http://www.portvisibility.co.uk/visibility/tools/myip.php'
    response = ''
    filePath = r'/path/to/file/ipAddress.txt'

    def __init__(self, filePath):
        request = urllib2.urlopen(self.url)
        self.response = json.loads(request.read())['host'] # url returns json
        self.filePath = filePath + '/ipAddress.txt'
        request.close()

    def CheckIp(self):
        date = self.__getDate()
        ipCount = 0
        mode = ''
        addressChanged = False

        if not os.path.isfile(self.filePath):
            mode = 'w+'
        else:
            mode = 'w'
            with open(self.filePath, 'r') as f:
                lines = f.readlines()

                if lines[0][:-2] == str(self.response):
                    # IP address hasn't changed
                    dateFromFile = datetime.datetime.strptime(lines[1][:-2], "%d-%m-%Y")
                    currentDate = datetime.datetime.strptime(date, "%d-%m-%Y")
                    ipCount = (currentDate-dateFromFile).days

                    # last recorded IP change date
                    date = lines[1][:-2]
                else:
                    # New IP address - count is 0
                    addressChanged = True
                    self.NewIp = self.response

        self.__writeToFile(date, ipCount, mode)

        return addressChanged

    def GetIp(self):
        return self.response

    def __writeToFile(self, date, currentIpCount, mode):
        f = open(self.filePath, mode)
        f.write(self.response + '\r\n')
        f.write(date + '\r\n')

        if currentIpCount == 1:
            f.write(str(currentIpCount) + ' day' + '\r\n')
        else:
            f.write(str(currentIpCount) + ' days' + '\r\n')
        f.close()


    def __getDate(self):
        now = datetime.datetime.now()
        date = str.format('{0}-{1}-{2}', now.day, now.month, now.year)

        return date
