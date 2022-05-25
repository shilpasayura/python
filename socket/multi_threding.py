import threading
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 3:
      time.sleep(delay)
      count += 1
      t=time.ctime(time.time())
      print (threadName,t, delay )

# Create two threads as follows
try:
   x = threading.Thread(target = print_time, args = ("Thread-1", 4 ))
   y = threading.Thread(target = print_time, args = ("Thread-2", 2 ))
   z = threading.Thread(target = print_time, args = ("Thread-3", 1 ))
   p = threading.Thread(target = print_time, args = ("Thread-4", 3 ))
   x.start()
   y.start()
   z.start()
   p.start()
except:
   print ("Error: unable to start thread")
ctr=0

while 5 > 2:
   pass
  
