import time
my_time = int(input("Enter the time in seconds "))
for x in range(my_time,0,-1):
    seconds = x % 60 #adding %60 so that seconds does not go over 60
    minutes = int(x/60) % 60 #adding % 60 so that minutes does not go over 60
    hours = int(x/3600)
    print(f"{hours}:{minutes:02}:{seconds:02}") #:02 will add 0 padding
    time.sleep(1)
print("Times UP!")