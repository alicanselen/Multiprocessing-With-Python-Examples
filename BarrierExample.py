from threading import Barrier , Thread
import time
bariyer = Barrier(2)

def fonk(isim , bekleme_suresi):
  global bariyer
  for i in range (2):
    print(f"{isim} calisiyor")
    time.sleep(bekleme_suresi)
    print(f"{isim} bariyerde bekliyor")
    bariyer.wait()
  print(f"{isim} bitti")
kirmizi=Thread(target=fonk , args = ("kirmizi" , 5))
mavi = Thread(target =fonk , args =("mavi" , 10))
kirmizi.start()
mavi.start()
kirmizi.join()
mavi.join()
print("sonlandi")

#palindrom sayilari yazan program 1-10000

liste2=[]
bari=Barrier(2)

def palindrom():
  global liste2
  global bari
  for i in range(1,10001):
    str_i=str(i)
    if(str_i==str_i[::-1]):
      liste2.append(str_i)
      bari.wait()

t1=Thread(target=palindrom)
t2=Thread(target= palindrom)

t1.start()
t2.start()

t1.join()
t2.join()

print(*liste2)


