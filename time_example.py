from datetime import time, date

meeting = time(hour=11, minute=15, second=0)
print(meeting)

end_time = time(hour=12, minute=30)
print(end_time)

iso_time = 'T11:15:00'
_time = time.fromisoformat(iso_time)
print(_time)

iso_date = '2025-04-03'
_date = date.fromisoformat(iso_date)
print(_date)