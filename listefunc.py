#verilen bir liste içindeki en büyük değeri veren python kodunu  fonksiyon kullanarak yazınız.

def func(*args):
    max=args[0]
    for i in args:
        for i in range(len(args)):
            if(args[i]>max):
                max=args[i]
                i+=1
    return(max)

liste=[1,2,5,90,8,156,78]
a=func(*liste)
print(a)



    
        
       


