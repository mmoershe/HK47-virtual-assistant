from beautiful_date import *
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event


gc = GoogleCalendar(credentials_path = "auth\\credentials.json")    


start = (30/Jun/2023)[12:00]
end = (30/Jun/2023)[14:00]

event = Event("Test1", start=start, end=end)

event = gc.add_event(event)