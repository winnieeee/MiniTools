#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:20:57 2020

@author: wanyingxu
"""

import os
import time


def countdown(t):
    x = t
    while t > 0:
        m, s = divmod(t, 60)
        time_left = ' ' + str(m).zfill(2) + ':' + str(s).zfill(2)
        print(time_left + ' out of %i minutes'%int(x/60), end = '\r', flush = True)
        time.sleep(1)
        t -= 1

    
    
if __name__ == '__main__':
    
    i = 1
    while(True):
        print('%i tomatoes                                      '%i)
    
        t_work = 45*60
        t_relax = 45*60
        os.system('say "Start Working"')
        countdown(t_work)
        os.system('say "Stand Up and Move"')
        countdown(t_relax)
        
        i += 1