import time
n=int(input("Enter the number:"))
for x in reversed(range(1,n+1)):
    print(f"00:00:0{x}")
    time.sleep(1)
print("⏰⏰⏰Time's up⏰⏰⏰")