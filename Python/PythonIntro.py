import time
import webbrowser

minute = 60
hour = minute*60

print("This program started on "+time.ctime())
for x in range(0, 3):
    time.sleep(2*hour)
    webbrowser.open("https://www.youtube.com/watch?v=Da4V5vKcGl8")

print "execution complete"
