import time
running = True
start_time=time.time()
#print("start_time:{}".format(start_time))
while running:
    now_time = time.time()
    #print("Now time:{}".format(now_time))
    seconds_elapsed=int(time.time()-start_time)
    print("seconds_elapsed:{}".format(seconds_elapsed))
    if seconds_elapsed == 3:
        start_time = time.time()
        print("Start time:{}".format(start_time))
