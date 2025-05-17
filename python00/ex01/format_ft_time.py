import time

curr = time.time()
formatted_curr = "{:,.2f}".format(curr)
science_curr = "{:e}".format(curr)
date = time.strftime("%b %d %Y")
print("Seconds since January 1, 1970:", formatted_curr, "or", science_curr, "in scientific notation")
print(date)