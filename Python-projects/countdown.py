import time
secs = int(input("Enter time in seconds: "))
while secs:
    print(f"Time left: {secs} sec", end="\r")
    time.sleep(1)
    secs -= 1
print("Time's up!")