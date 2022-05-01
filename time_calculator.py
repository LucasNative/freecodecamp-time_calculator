week = {
    "monday" : 0,
    "tuesday" : 1,
    "wednesday" : 2,
    "thursday" : 3,
    "friday" : 4,
    "saturday" : 5,
    "sunday:" : 6
    }

week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def sort_data(time, time_passed):
    temp_t, period = time.split()
    list_args = list((temp_t.split(":") + time_passed.split(":")))
    sorted_list = list(map(lambda x: int(x), list_args))
    sorted_list.append(period)
    return sorted_list

def change_period(period):
	return "AM" if period == "PM" else "PM"

def calc_minute(minute, add_minute):
    hour = 0
    if (minute + add_minute > 60):
        minute += add_minute
        while(minute >= 60):
            minute -= 60
            hour += 1
    elif (minute + add_minute == 60):
        hour += 1
        minute = 0
    else:
        minute += add_minute
    return [hour, minute]

def calc_hours(hour, add_hour, time_period, res_hour):
    period = time_period
    add_hour += res_hour
    days_passed = " "
    count_days = 0
    if (hour + add_hour >=12):
        hour += add_hour
        if (period == "PM"):
            count_days += 0.5
        while(hour > 12):
            hour -= 12
            count_days += 1 / 2
            period = change_period(period)
        count_days = int(count_days + 0.5)
        if (count_days >= 2):
            days_passed = "({} days later)".format(count_days)
        if(hour == 12):
            period = change_period(period)
        if (count_days < 2 and period == "AM"):
            days_passed = "(next day)"
        if (count_days < 2 and period == "PM"):
            count_days = 0
    else:
        hour += add_hour
    return [days_passed, hour, period, count_days]

def set_weekday(initial_day, days):
    weekend_d = None
    amount_days = week[initial_day] + days
    if (amount_days > 7):
        while (amount_days >= 7):
            amount_days -= 7
    weekend_d = week_list[amount_days]
    return weekend_d

def add_time(time, time_passed, setday = 0):
    hour, minute, add_hour, add_minute, period = sort_data(time, time_passed)
    res_hour, res_minute = calc_minute(minute, add_minute)
    passed_day, new_hour, cycle, days_counted = calc_hours(hour, add_hour, period, res_hour)
    today = setday
    if (today != 0):
        today = setday.lower()
        week_day = set_weekday(today, days_counted)
        if (passed_day == " "):
            return "{}:{:0>2} {}, {}".format(new_hour, res_minute, cycle, week_day)
        return "{}:{:0>2} {}, {} {}".format(new_hour, res_minute, cycle, week_day, passed_day)
    if (passed_day == " "):
        return "{}:{:0>2} {}".format(new_hour, res_minute, cycle)
    return "{}:{:0>2} {} {}".format(new_hour, res_minute, cycle, passed_day)

print(add_time("3:00 PM", "3:10"))

print(add_time("11:30 AM", "2:32", "Monday"))

print(add_time("11:43 AM", "00:20"))

print(add_time("10:10 PM", "3:30"))

print(add_time("11:43 PM", "24:20", "tueSday"))

print(add_time("6:30 PM", "205:12"))
