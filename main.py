import time
import sys

countdown_time = 10

while countdown_time > 0:
    print(countdown_time)
    countdown_time -= 1
    time.sleep(1)

print("Đếm ngược đã xong")
sys.exit(0)
