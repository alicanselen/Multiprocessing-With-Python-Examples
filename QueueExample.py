import time
from queue import Queue
from threading import Thread

def gonderici(kuyruk):
  while True:
    kuyruk.put(["Alican Selen",time.time()])
    print("selam")

def alici(kuyruk):
  while True:
    print(kuyruk.get())
    time.sleep(1)

qq=Queue(maxsize=100)
t1=Thread(target=gonderici,args=(qq,))
t2=Thread(target=alici,args=(qq,))
t1.start()
t2.start()
