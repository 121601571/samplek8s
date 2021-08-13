import threading

cnt = 0
def cntinc():
    global cnt
    for i in range(1,100000):
        cnt += 1

def cntdec():
    global cnt
    for i in range(1,100000):
        cnt -= 1;

for i in range(1,2):
    t1 = threading.Thread(target=cntinc )
    t2 = threading.Thread(target=cntdec )
    t1.start()
    t2.start()
    t1.join()
    t2.join()


print(cnt)
