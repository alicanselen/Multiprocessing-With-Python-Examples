import time
from multiprocessing import Pipe
from threading import Thread

def ping(pipe_baglantisi):
  while True:
    txt = pipe_baglantisi.recv()
    print(txt)
    pipe_baglantisi.send("pong")
    time.sleep(1)

def pong(pipe_baglantisi):
  while True:
    txt = pipe_baglantisi.recv()
    print(txt)
    pipe_baglantisi.send("ping")
    time.sleep(1)

sona ,sonb=Pipe()
t1=Thread(target=ping , args=(sona,))
t2=Thread(target=pong , args=(sonb,))
t1.start()
t2.start()
