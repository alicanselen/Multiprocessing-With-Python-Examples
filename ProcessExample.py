import multiprocessing
import time

def gonderici(qq):

    qq.put("Merhaba")
    print("MEsaj Gonderildi")
    #time.sleep(1)

def alici(qq):

    txt = qq.get()
    print(txt)

if __name__ == "__main__":
    QQ = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=alici, args=(QQ,))
    p2 = multiprocessing.Process(target=gonderici, args=(QQ,))

    p1.start()
    p2.start()

    p1.join()  # p1 sürecinin bitmesini bekle
    p2.join()  # p2 sürecinin bitmesini bekle

