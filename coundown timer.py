import time

total_seconds = int(input("Enter countdown time in seconds: "))

for remaining in range(total_seconds, 0, -1):
    secs = remaining % 60
    mins = int((remaining / 60) % 60)
    hrs  = int(remaining / 3600)
    print(f"{hrs:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("\n\nTimes UP.\n")
print("🔥 WEELLLL!! Done!")
