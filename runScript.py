#!usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:38:14 2014

@author: RedSpiderMkV
"""

from IpRetriever import IpRetriever

def main():
    ipRetriever = IpRetriever()
    
    ipRetriever.CheckIp()
    print ipRetriever.GetIp()
    
if __name__ == "__main__":
    main()