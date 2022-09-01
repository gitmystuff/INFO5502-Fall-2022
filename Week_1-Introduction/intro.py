#!/usr/bin/env python
# coding: utf-8

def hello():
    return str('Hello There!')
    
class Introduction:
    
    def __init__(self, my_name, your_name):
        self.my_name = my_name
        self.your_name = your_name
        
    def talk_to_me(self):
        return f'Hi {self.your_name}. I am {self.my_name}'
    