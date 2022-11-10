def day_of_day(date):
    date_list = date.split("-")
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])

    leap = False
    if year % 4 == 0:
        pass

    months = [
        (1, 31),
        (2, 28),
        (3, 31),
        (4, 30),
        (5, 31),
        (6, 30),
        (7, 31),
        (8, 31),
        (9, 30),
        (10, 31),
        (11, 30),
        (12, 31),
    ]

    count = 1
    ans = 0
    while count < month:
        ans += months[count - 1][1]
        count += 1
    ans += day
    if leap:
        ans += 1
    return ans


print(day_of_day("2019-01-09"))
print(day_of_day("2019-02-10"))
# print(day_of_day("2019-02-10"))
