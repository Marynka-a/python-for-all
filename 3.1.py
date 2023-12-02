hrs = input("Enter Hours:")
h = float(hrs)
x = 40
rate = input("Enter per hours")
r = float(rate)
if h <= 40:
    pay = (x*r)
elif h > 40:
    pay = (x*r+(h-x)*1.5*r)
print(pay)