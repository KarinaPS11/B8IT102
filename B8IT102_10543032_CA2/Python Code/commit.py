# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:21:02 2020

@author: 10543032
"""

class Commit:
    
    def __init__(self, details, comment = '', changedpaths = ''):
        self.__id = details[0]
        self.__author = details[1]
        self.__date_time= details[2]
        self.__date =  details[2].split(' ')[0]
        self.__time =  details[2].split(' ')[1]
        self.__day =  details[2].split(' ')[3].lstrip('(').rstrip(',')
        self.__commentlines = details[3]
        self.__numlines = details[3].split(' ')[0]
        self.__commentlines = details[3]
        self.__comment = comment
        
    def __str__(self):
        return'"{0}", "{1}", "{2}","{3}","{4}","{5}","{6}", \n'.format(
                self.__id, 
                self.__author,
                self.__date, 
                self.__time,
                self.__day,
                self.__numlines,
                self.__comment)
                