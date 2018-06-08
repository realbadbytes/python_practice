# __init__ and run are the two methods that should be modified in threading lib
# start() calls run(), run is responsible for calling our target function

import time
import threading

class MyThread(threading.Thread):
    def run(self):
        thread_name = self.getName()
        print '{} has started'.format(thread_name)
        try:
            if self.__target:
                # unpack variable length args to target function
                self.__target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs
            print '{} has finished'.format(thread_name)

def sleeper(n, name):
    print 'thread {} sleeping for {} seconds'.format(n, name)
    time.sleep(n)

for i in range(4):
    t = MyThread(target=sleeper, 
                 name='thread_{}'.format(i), 
                 args=(1, 'thread_{}'.format(i)))
    t.start()
