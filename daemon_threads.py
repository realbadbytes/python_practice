import threading
import time

total = 4

# item creator
def create_items():
    global total
    for i in range(10):
        time.sleep(1)
        print 'added item'
        total += 1
    print 'finished creation'

# item limiter
def limit_item_creation():
    global total
    while True:
        if total > 5:
            print 'overload'
            total -= 3
            print 'removed 3 items'
        else:
            time.sleep(1)
            print 'waiting'

creator_1 = threading.Thread(target=create_items)
creator_2 = threading.Thread(target=create_items)
limiter = threading.Thread(target = limit_item_creation)
limiter.daemon = True

thread_list = []
thread_list.append(creator_1)
thread_list.append(creator_2)
thread_list.append(limiter)

# start all threads
creator_1.start()
creator_2.start()
limiter.start()

# run to completion
# limiter will continue to run, even after creator threads
# have exhausted their iterators, forever printing 'waiting'
# fix: use daemon threads
# daemon is a thread attribute, daemon is default False
# daemon=True ends thread when main terminates

# stackoverflow.com/questions/47415918/why-is-it-bad-to-call-join-on-a-daemon-thread
# ** we do not join() a daemon thread because that implies the join will block 
# until the daemon thread ends, which assuming its a well designed daemon thread, is never. **

creator_1.join()
creator_2.join()

print 'ending total is {}'.format(total)








