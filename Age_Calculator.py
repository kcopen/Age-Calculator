'''
Created on Sep 12, 2019

@author: Kyle
'''
import datetime

def is_leap_year(year):
    if (year % 100 == 0):
        if(year % 400 == 0):
            return True
        else:
            return False
    elif(year % 4 == 0):
        return True
    else:
        return False
        
def get_days_in_year(year):
    if (is_leap_year(year)):
        return 366
    else:
        return 365
        
def get_days_in_month(month, year):
    if (month == 1 or month == 3 or month ==  5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif (month == 2 or month == 4 or month ==  6 or month == 9 or month == 11):
        return 30
    else:
        if (is_leap_year(year)):
            return 29
        else:
            return 28
        
def get_age_in_days(birth_month, birth_day, birth_year, current_month, current_day, current_year):
    age_in_days = 0
    temp_month = 1
    temp_year = current_year
    
    while (temp_month < current_month):
        age_in_days += get_days_in_month(temp_month, temp_year)
        temp_month +=1
    
    temp_year -= 1
    age_in_days += current_day - 1
    
    while (temp_year > birth_year):
        age_in_days += get_days_in_year(temp_year)
        temp_year -= 1
    
    temp_month = 1
    days_until_birthday_in_birth_year = 0
    
    while (temp_month < birth_month):
        days_until_birthday_in_birth_year += get_days_in_month(temp_month, temp_year)
        temp_month +=1
    
    days_until_birthday_in_birth_year += birth_day
    age_in_days += get_days_in_year(temp_year) - days_until_birthday_in_birth_year - 1   
    
    return age_in_days
        
def get_age_in_years(birth_month, birth_day, birth_year, current_month, current_day, current_year):
    age_in_years = current_year - birth_year
    
    if (current_month - birth_month < 0):
        age_in_years -= 1
    elif (current_month - birth_month == 0):
        if (current_day - birth_day < 0):
            age_in_years -= 1
    return age_in_years

if __name__ == '__main__':
    currentYear = datetime.datetime.now().year
    currentMonth = datetime.datetime.now().month
    currentDay = datetime.datetime.now().day
 
    birthMonth = int(input("birth month: "))
    birthDay = int(input("birth day: "))
    birthYear = int(input("birth year: "))
    
    print("Your current age in years is " + str(get_age_in_years(birthMonth, birthDay, birthYear, currentMonth, currentDay, currentYear)))
    print("Your current age in days is " + str(get_age_in_days(birthMonth, birthDay, birthYear, currentMonth, currentDay, currentYear)))
    
    pass