import threading
import logging

lock = threading.Lock()
def threadwith(lock):
    with lock:
        print('\n Lock With Block \n')
        for i in range(5):
            print ("With block i=",i)
            print('\n')
        print(threading.currentThread().getName())


def threadacquire(lock):
    try:
        lock.acquire(blocking=True)
        print('\n Lock Acquire Block \n')
        for i in range(5):
            print ("Acquire block i=",i)
            print('\n')
        print(threading.currentThread().getName())
    finally:
        lock.release()


tw = threading.Thread(target=threadwith, args=(lock,))
ta = threading.Thread(target=threadacquire, args=(lock,))

tw.start()
ta.start()

#threadwith(lock)
#threadacquire(lock)