#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        SmtpProviderFactory
# Purpose:     Retrieve the SMTP provider for the email address entered.
#
# Author:      RedSpiderMkV
#
# Created:     Sat Jun 11 20:05:25 2016
# Copyright:   (c) RedSpiderMkV 2016
#-------------------------------------------------------------------------------

from SmtpProviders import SmtpProviders

class SmtpProviderFactory:
    ''' SmtpProviderFactory - retrieve the SMTP provider for a specified
        email address. '''
        
    @classmethod
    def GetProvider(self, userAccount):
        ''' Get SMTP provider for the specified email address.

            Args:
                userAccount - email address as a string.
                
            Returns:
                SmtpProvider - SMTP provider for email address.
                If email address is invalid or not supported, returns None. '''
        
        emailProvider = None
        
        try:
            emailProvider = userAccount.split('@')[1].split('.')[0]
        except IndexError:
            print 'Invalid email'
            return None

        outlook = ['hotmail', 'live', 'outlook']
        gmail = ['gmail', 'googlemail']
        yahoo = ['yahoo']
        
        if emailProvider in outlook:
            return SmtpProviders.OUTLOOK
        elif emailProvider in gmail:
            return SmtpProviders.GMAIL
        elif emailProvider in yahoo:
            return SmtpProviders.YAHOO
        
        return None
