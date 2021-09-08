import datetime

# ------------

def add(moment):
    return moment + datetime.timedelta(0, 1000000000)

# --- quick test
# print(add(datetime.datetime(2011, 4, 25, 0, 0)))
