def day_of_day(date):
    date_list = date.split("-")
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])

    leap = True if year % 4 == 0 else False
