# T.Lehtsalu
# 01.11.2022
# Harjutus09

import datetime
import locale






aeg = datetime.datetime.now()
print(aeg.strftime("%d. %B %Y"))

locale.setlocale(locale.LC_ALL, "et_EE")

print(aeg.strftime("%d. %B %Y"))

