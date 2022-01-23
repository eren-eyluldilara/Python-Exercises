#yazılımcıdan kaynaklanan hatalar
#yazılımsal hatalar
#mantıksal hatalar

try:
     -komutlar #try kısmı çalışır , eğer hata varsa program excepti çalıştırır ve oradaki bilgiyi print eder,hata bulunduğu an excepte geçiyor
except Exception as hata:
    print("Bir hata oluştu",hata)
finally: #hata olsun olmasın mutlaka çalışır