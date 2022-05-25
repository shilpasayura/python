import threading
import time

def sleepy_man(secs, order):
    msg="Starting to sleep inside " + str(secs) + " " + str(order) + "\n"
    print(msg)
    time.sleep(secs)
    print("Woke up inside " , secs, order, "\n")

x = threading.Thread(target = sleepy_man, args = (4,1))
y = threading.Thread(target = sleepy_man, args = (2,2))
z = threading.Thread(target = sleepy_man, args = (1,3))
x.start()
y.start()
z.start()
print(threading.activeCount())
time.sleep(6)
print()
print('Done')
