import webbrowser
import time

total_breaks = 3
print(f"This program started on{time.ctime()}")

for _ in range(total_breaks):
    time.sleep(2 * 60 * 60)
    webbrowser.open("http://www.youtube.com")
