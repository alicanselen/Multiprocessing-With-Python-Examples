from threading import Thread , Lock , Condition ,Barrier
para =0
cv = Condition()
for i in range (10):
  def kazanan():
    global para , cv
    for i in range (1000000):
      cv.acquire()

      para+=10
      cv.notify()
      cv.release()

  def harcayan():
    global para,cv

    for i in range (500000):
      cv.acquire()
      while para< 20:
        cv.wait()
      para -=20
      if (para<0):
        print("para değeri negatiftir")
      cv.release()



  t1= Thread(target= kazanan)
  t2 = Thread(target = harcayan)

  t1.start()
  t2.start()
  t1.join
  t2.join

  print(f"kalan para : {para}")

#join ornegi

def fonk1():
  print("iş başladı")
  time.sleep(5)
  print("iş bitti")

def fonk2():
  print("fonksiyon 2 başladı")
  t = Thread(target = fonk1)
  t.start()
  t.join()
  print("fonksiyon 2 bitti")

if __name__ == '__main__':
  t2=Thread(target=fonk2)
  t2.start()
  t2.join()
  print("selam")

#1-10000 tam kare sayıları bulan kodu iki ya da 4 farklı thread ile yapalım
liste = []
lock = threading.Lock()
def kare_bul(baslangic , bitis):
  global liste
  for sayi in range(baslangic , bitis+1):
    if int(Math.sqrt(sayi))**2 == sayi:
      with lock:
        liste.append(sayi)
t1= Thread(target=kare_bul , args=(1,5000))
t2= Thread(target=kare_bul ,args=(5001,10000))
t1.start()
t2.start()

t1.join()
t2.join()

print(*liste)

liste1=set()

def tam_kare_bul():
  global liste1
  for i in range (1,10001):
    s=i*i
    if s<10001:
      liste1.add(s)


t3 = Thread(target = tam_kare_bul )
t4 = Thread(target= tam_kare_bul)

t3.start()
t4.start()

t3.join()
t4.join()

print(*liste1)

bariyer = Barrier(2)

def fonk(isim , bekleme_suresi):
  for i in range (10):
    print(f"{isim} calisiyor")
    time.sleep(bekleme_suresi)
    print(f"{isim} bariyerde bekliyor")
    bariyer.wait()
