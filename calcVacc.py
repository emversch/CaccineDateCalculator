import datetime as dt

def calcVacc(vaccin, date_letter, QVAX):
    """calculate vaccination dates"""
    
    wait_period = {
        "pfizer": 5,
        "jj": 0,
        "moderna": 4,
        "az": 8
    }
    wait_letter = 2 if QVAX == False else 0
    wait_protected = 4 if vaccin == "jj" else 2
    
    dose_1 = date_letter + dt.timedelta(weeks=wait_letter)
    dose_2 = dose_1 + dt.timedelta(weeks=wait_period[vaccin])
    protected = dose_2 + dt.timedelta(weeks=wait_protected)
    
    return [dose_1, dose_2, protected]