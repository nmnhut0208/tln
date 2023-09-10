import os
import sys

__all__ = ['Logger']

# class Logger to test print
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.text = "nhutnm4"

    def show(self):
        print(self.text)