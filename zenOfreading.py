import time

with open("C:\Projecten\Software Dev\Mapje 9\-read-files\README.md", "r") as file:
    for x in file:
        time.sleep(1)
        print(x, end="")