#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 
@author zhangbohan.dell@gmail.com
@function:
@create 1/10/2020 9:25 PM
"""
import logging

class Logger():
    def __init__(self,log_file="ncmdump.log",level=logging.INFO,formatter='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        self.log_file = log_file
        self.level = level
        self.formatter = formatter
        logging.basicConfig(level=self.level,filename=self.log_file,format=self.formatter)

    def getFroName(self,name="default"):
        logger = logging.getLogger(name)
        return logger

