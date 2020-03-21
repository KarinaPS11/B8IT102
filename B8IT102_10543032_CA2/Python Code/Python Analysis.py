# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:17:11 2020

@author: 10543032
"""


import operator
#Upload 
new_file = 'R:/10543032_CA2/commits.csv'

def get_data(new_file):
    data_file = open(new_file)
    data = data_file.readlines()
    data_file.close()
    return data

get_data(new_file)

data = get_data(new_file)

#Python Analysis

#How many times does each developer work?
def count_developers(data):
    no_developers = {}
    for row in data[1:]:
        # get column b the manufacturer and each time I see
        # a manufacturer add 1 to the list
        developer = row.strip().split(',')[1]
        if developer in no_developers:
            no_developers[developer] += 1
        else:
            no_developers[developer] = 1
        print(developer)
    for make in no_developers:
       print('{0} : {1}'.format(make, no_developers[make]))
    return no_developers

#Who makes the most changes? 
def get_hard_worker(no_developers):
    sorted_d = sorted(no_developers.items(),
        key=operator.itemgetter(1), reverse=True)
    print('Dictionary in ascending order by value : ', sorted_d)
    print('Get the developer who makes the most adjusments to the code ', sorted_d[0])

#List of all the developers
count_developers(data)

developer_no = count_developers(data)

#creates a list in ascending order of the most ammendments made and who makes the most.
get_hard_worker(developer_no)


#What dates were the most commonly worked on?
def count_dates(data):
    num_dates = {}
    for row in data[1:]:
        # get column b the manufacturer and each time I see
        # a manufacturer add 1 to the list
        date = row.strip().split(',')[2]
        if date in num_dates:
            num_dates[date] += 1
        else:
            num_dates[date] = 1
        print(date)
    for each_date in num_dates:
       print('{0} : {1}'.format(each_date, num_dates[each_date]))
    return num_dates

#What date was the most edited day ?
def most_edited_date(num_days):
    sorted_d = sorted(num_days.items(),
        key=operator.itemgetter(1), reverse=True)
    print('Dictionary in ascending order by value : ', sorted_d)
    print('Get the most edited day of the set ', sorted_d[0])

#list of all dates 
count_dates(data)

#count of all dates that have ammendement
popular_date = count_dates(data)

#List and the mos populat date!
most_edited_date(popular_date)


#What day of the week is the most commonly worked on?
def count_days(data):
    num_days = {}
    for row in data[1:]:
        # get column b the manufacturer and each time I see
        # a manufacturer add 1 to the list
        day = row.strip().split(',')[4]   
        if day in num_days:
            num_days[day] += 1
        else:
            num_days[day] = 1
        print(day)
    for each_day in num_days:
       print('{0} : {1}'.format(each_day, num_days[each_day]))
    return num_days

#What date was the most edited day ?
def most_edited_day(no_days):
    sorted_d = sorted(no_days.items(),
        key=operator.itemgetter(1), reverse=True)
    print('Dictionary in ascending order by value : ', sorted_d)
    print('Get the most edited day of the set ', sorted_d[0])
    
#List of all the days of the week that the code was ammended
count_days(data)

#count all the days that the code has been ammended on 
popular_day = count_days(data)

#List and the mos populat day!
most_edited_day(popular_day)
    


#How many lines on average are being edited.
def calculate_average_num_lines(data):
    lines = data[1:]
    numlines= len(lines)
    total_lines = 0
    # calculate average wheelbase
    for row in data[1:]:
        # remove line ending with strip
        # split string by comma separator into list
        # process index 3, i.e. column D
        total_lines += float(row.strip().split(',')[5])
    
    average_numlines = total_lines/ numlines
    print('Average Number of Lines being edited: {0}'.format(average_numlines))
    
calculate_average_num_lines(data)
