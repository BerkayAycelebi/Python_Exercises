from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,"Turkish_Turkey")

#a=datetime.now()
#a=a.year
#a=datetime.now()
#a=a.day()
#a=datetime.now()
#a=a.month()
#a=datetime.now()
#a=a.hour()
#a=datetime.now()
#a=a.minute()

a=datetime.now()

exact_history=datetime.strftime(a,"%B")
print(exact_history)