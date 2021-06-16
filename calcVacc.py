# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:32:57 2021

@author: Edward
"""

import datetime

def calcVacc(vaccin, date_letter, QVAX):
    """calculate vaccination dates"""
    
    wait_period = {
        "letter": 14,
        "pfizer": 5*7,
        "moderna": 4*7,
        "az": 8*7,
        "jj": 0,
        "protected": 14
    }
    wait_protected = 4*7 if vaccin == "jj" else 14
    
    if QVAX == False:
        dose_1 = date_letter + datetime.timedelta(days=wait_period["letter"])
    else:
        dose_1 = date_letter
        
    dose_2 = dose_1 + datetime.timedelta(days=wait_period[vaccin])
    
    protected = dose_2 +datetime.timedelta(days=wait_protected)
    
    return [dose_1, dose_2, protected]