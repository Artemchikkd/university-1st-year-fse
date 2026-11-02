N = int(input("Введите количество секунд: "))

seconds_in_day = N % 86400
hours = seconds_in_day // 3600
minutes = (seconds_in_day % 3600) // 60
seconds = seconds_in_day % 60

print("{}:{:02d}:{:02d}".format(hours, minutes, seconds))
