from datetime import datetime

from pytz import timezone

chile = timezone('America/Santiago')
chileDate = datetime.now(chile)
final = chileDate.strftime('%d/%m/%Y %H:%M')
print(final)