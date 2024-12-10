#compound interest A = P(1+r/n)^t
# A = final amount
# P = initial principal balance
# r = interest rate in decimel
# t = number of time period elapsed
# n = number of times interest applied per time period
principle = 0
rate = 0
time =0
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero ")
    else:
        break


while True:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
        print("rate can't be less than or equal to zero ")
    else:
        break

while True:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("time can't be less than or equal to zero ")
    else:
        break

total = principle * pow(( 1 + rate /100) , time)
print(f"Your banlence after {time} year/s is ${total:.2f} ")
