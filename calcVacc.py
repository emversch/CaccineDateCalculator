import datetime as dt

def calcVacc(vaccin, date_letter, QVAX):
    """calculate vaccination dates"""
    
    wait_period_weeks = {
        "letter": 2,
        "pfizer": 5,
        "moderna": 4,
        "az": 8,
        "jj": 0
    }
    wait_protected = 4 if vaccin == "jj" else 2
    
    dose_1 = date_letter;
    dose_1 += dt.timedelta(weeks=wait_period_weeks["letter"]) if QVAX == False else dt.timedelta(0)
        
    dose_2 = dose_1 + dt.timedelta(weeks=wait_period_weeks[vaccin])
    
    protected = dose_2 + dt.timedelta(weeks=wait_protected)
    
    return [dose_1, dose_2, protected]