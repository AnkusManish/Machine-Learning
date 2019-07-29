#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 14:24:01 2019

@author: ankusmanish
"""

import os
#getegid() method returns the effective group id
print("Effective group id: ",os.getegid())
#geteuid() method returns the effective user id
print("Effective user id: ",os.geteuid())
#getgid() method returns  returns the real group id
print("Real group id: ",os.getgid())
#getgroups() method returns the supplemental group ids
print("List of supplemental group ids: ",os.getgroups())
