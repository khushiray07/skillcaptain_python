import threading
import time

def msg_one():
    print("Message 1: Preparing the system...")

def msg_two():
    print("Message 2: Processing your request...")

def msg_three():
    print("Message 3: Task completed successfully!")

t1 = threading.Thread(target=msg_one)
t2 = threading.Thread(target=msg_two)
t3 = threading.Thread(target=msg_three)

t1.start()
t1.join()   

t2.start()
t2.join()   

t3.start()
t3.join()   

print("\n All messages printed in correct order!")
