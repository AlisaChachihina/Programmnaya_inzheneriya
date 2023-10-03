import datetime
import time
def main():
    print(datetime.datetime.now().time())
for i in range(5):
    main()
    time.sleep(1)