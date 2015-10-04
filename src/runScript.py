#!usr/bin/python

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:38:14 2014

@author: RedSpiderMkV
"""

from IpRetrieverLib import IpRetriever

def main():
    ipRetriever = IpRetriever(r'../')
    
    ipRetriever.CheckIp()
    
if __name__ == "__main__":
    main()