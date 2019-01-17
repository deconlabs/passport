# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:22:51 2019

@author: user
"""

from tensorboardX import SummaryWriter
writer = SummaryWriter()

for i in range(100):
    writer.add_scalar('test',pow(i,2),i)