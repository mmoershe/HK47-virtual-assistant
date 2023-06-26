from beautiful_date import * 

today = BeautifulDate.today()+0*days
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

print(weekdays[today.weekday()][:3])
