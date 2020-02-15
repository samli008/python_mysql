#time module
import time

print('start...')
time.sleep(5)
print('end...')

# a tuple of 9 integers

>>> time.gmtime(0)
time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
>>> time.gmtime()
time.struct_time(tm_year=2020, tm_mon=2, tm_mday=15, tm_hour=12, tm_min=7, tm_sec=46, tm_wday=5, tm_yday=46, tm_isdst=0)


