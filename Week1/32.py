#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:24:01 2019

@author: ankusmanish
"""

import os
print("Effective group id: ",os.getegid())
print("Effective user id: ",os.geteuid())
print("Real group id: ",os.getgid())
print("List of supplemental group ids: ",os.getgroups())
