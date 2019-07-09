import threading
import logging

lock = threading.Lock()
p = 0

def threadwith(lock):
    global p
    with lock:
        print('\n Lock With Block \n')
        for i in range(5):
            p=p+i
            print ("With block p=",p)
            print('\n')
        print(threading.currentThread().getName())


def threadacquire(lock):
    global p
    try:
        lock.acquire(blocking=True)
        print('\n Lock Acquire Block \n')
        for i in range(5):
            p=p+i
            print ("Acquire block p=",p)
            print('\n')
        print(threading.currentThread().getName())
    finally:
        lock.release()

tw = threading.Thread(target=threadwith, args=(lock,))
ta = threading.Thread(target=threadacquire, args=(lock,))

tw.start()
ta.start() 