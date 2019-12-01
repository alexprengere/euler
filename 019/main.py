from datetime import date, timedelta
DAY = timedelta(days=1)

start_date = date(1901, 1, 1)
end_date = date(2000, 12, 31)

total = 0
d = start_date
while d <= end_date:
    if d.isoweekday() == 7 and d.day == 1:
        total += 1
    d = d + 1 * DAY

print(total)
