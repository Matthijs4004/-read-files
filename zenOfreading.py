import time

file = open("C:\Projecten\Software Dev\Mapje 9\-read-files\README.md", "r")

for x in file:
    time.sleep(1)
    print(x)