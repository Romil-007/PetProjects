totalday = 0
sunday = 0
date = int(input("Day : "))
month = int(input("Month : "))
year = int(input("Year :  "))

day = input("What is today's day(M/Tu/W/Th/F/Sa/Su) : ")
l = ["M" , "TU" , "W" , "TH" , "F" , "SA" , "SU"]
while(not(day.upper() in l)):
    day = input("What is today's day(M/Tu/W/Th/F/Sa/Su) : ")

date2 = int(input("What is today's date : ")) 
month2 = int(input("What is today's Month : "))
year2 = int(input("What is right now year? : "))

if(month2 <= 12):
    if(month2 == 1):
        totalday += 0+date2
    if(month2 == 2):
        totalday += 31+date2
    if(month2 == 3):
        totalday += 31+28+date2
    if(month2 == 4):
        totalday += 31+28+31+date2
    if(month2 == 5):
        totalday += 31+28+31+30+date2
    if(month2 == 6):
        totalday += 31+28+31+30+31+date2
    if(month2 == 7):
        totalday += 31+28+31+30+31+30+date2
    if(month2 == 8):
        totalday += 31+28+31+30+31+30+31+date2
    if(month2 == 9):
        totalday += 31+28+31+30+31+30+31+31+date2
    if(month2 == 10):
        totalday += 31+28+31+30+31+30+31+31+30+date2
    if(month2 == 11):
        totalday += 31+28+31+30+31+30+31+31+30+31+date2
    if(month2 == 12):
        totalday += 31+28+31+30+31+30+31+31+30+31+30+date2


if(month <= 12):
    if(month == 1):
        totalday += 31+28+31+30+31+30+31+31+30+31+30+(31-date)+1
    if(month == 2):
        if(date == 29):
            totalday += 31+30+31+30+31+31+30+31+30+31+1
        else:
            totalday += 31+30+31+30+31+31+30+31+30+31+(28-date)+1
    if(month == 3):
        totalday += 31+30+31+30+31+31+30+31+30+(31-date)+1
    if(month == 4):
        totalday += 31+30+31+30+31+31+30+31+(30-date)+1
    if(month == 5):
        totalday += 31+30+31+30+31+31+30+(31-date)+1
    if(month == 6):
        totalday += 31+30+31+30+31+31+(30-date)+1
    if(month == 7):
        totalday += 31+30+31+30+31+(31-date)+1
    if(month == 8):
        totalday += 31+30+31+30+(31-date)+1
    if(month == 9):
        totalday += 31+30+31+(30-date)+1
    if(month == 10):
        totalday += 31+30+(31-date)+1
    if(month == 11):
        totalday += 31+(30-date)+1
    if(month == 12):
        totalday += (31-date)+1



totyear = year2-year-1

totalday += (totyear*365)

if((year % 400 == 0) or (year % 4 == 0 and (not(year % 100 == 0)))):
    
    if(month == 2):
        if(not(date == 29)):
            totalday += 1


if((year2 % 400 == 0) or (year2 % 4 == 0 and (not(year2 % 100 == 0)))):
    if(month2 >= 2):
        if(month2 == 2 and date2 == 29):

            totalday += 1
        else:
            if(month2 >= 2):
                totalday += 1
            
            


for i in range(year+1 , year2 , 1):
    if((i % 400 == 0) or (i % 4 == 0 and (not(i % 100 == 0)))):
        totalday += 1
    else:
        continue

if(day.upper() == "M"):
    totalday -= 2
    sunday += 1
elif(day.upper() == "TU"):
    totalday -= 3
    sunday += 1
elif(day.upper() == "W"):
    totalday -= 4
    sunday += 1
elif(day.upper() == "TH"):
    totalday -= 5
    sunday += 1
elif(day.upper() == "F"):
    totalday -= 6
    sunday += 1
elif(day.upper() == "SA"):
    totalday -= 7
    sunday += 1
else:
    sunday += 1
    totalday -= 1

sunday += int(totalday/7)

print(sunday)