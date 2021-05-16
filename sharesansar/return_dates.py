from datetime import date, timedelta


# Compute the dates
def return_dates(sdate=date, edate=date):
    dates_list = []
    delta = edate - sdate      
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        dates_list.append(str(day))
    return dates_list
