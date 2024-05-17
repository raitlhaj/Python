
from datetime import datetime, timedelta

def yesterday(frmt = '%m/%d/%Y', string = True):
    yesterday = datetime.now() - timedelta(1)
    if string:
     return yesterday.strftime(frmt)
    return yesterday