#1500 (1500 dahil) ve 2700 arasında (2700 dahil), 7 ile bölünebilen aynı zamanda 5 in katı olan sayıları yazdırınız.
for x in range(1500,2701):
    if((x%7==0)and(x%5==0)):
        print(x,end=" ")