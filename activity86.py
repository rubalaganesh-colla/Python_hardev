import random 
import time 
def getrandomDate(startDate,endDate):
    print("printing random date between",startDate,"and",endDate)
    randomGenerator= random.random()
    dateformat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate,dateformat))
    endTime = time.mktime(time.strptime(endDate,dateformat))

    startTime = startTime + randomGenerator* (endTime - startTime)
    endTime = time.mktime(time.strptime(endDate,dateformat))
    return randomGenerator
print("Random date is:",getrandomDate("1/1/2020","12/31/2020"))
    