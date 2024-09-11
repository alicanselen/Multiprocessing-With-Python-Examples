import multiprocessing
import time
from multiprocessing import Pipe
from threading import Thread

def gonderici(pipe_baglanti):
  while True:
    time.sleep(1)
    pipe_baglanti.send("Merhaba ben Alican")

def alici(pipe_baglanti):
  while True:
    print(pipe_baglanti.recv())
    time.sleep(1)

son1 , son2= multiprocessing.Pipe(duplex=False)
t1 = Thread(target=gonderici, args=(son1,))
t2 = Thread(target=alici, args=(son2,))
t1.start()
t2.start()
