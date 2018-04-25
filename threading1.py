import threading
import time

def sleeper(n, name):
    print 'I am {}. Sleeping for {} seconds'.format(name, n)
    time.sleep(n)
    print '{} has woken up'.format(name)

'''
t = threading.Thread(target=sleeper, name='thread_1', args=(5, 'thread_1'))
t.start()
print "past t.start()"
t.join()
print "past t.join()"
'''

threads_list = []

start = time.time()

for i in range(5):
    t = threading.Thread(target = sleeper, 
                        name = 'thread_{}'.format(i), \
                        args=(2, 'thread_{}'.format(i)))
    t.start()
    print '{} has started'.format(t.name)
    threads_list.append(t)

# run all threads to completion
for t in threads_list:
    t.join()

end = time.time()

print 'exec is finished, time elapsed {}'.format(end-start)
