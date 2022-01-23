liste=[1,2,5,90,8,156,78]
def max_val(*args):
    eb=0
    for i in args:
        if i>eb:
            eb=i
    return eb

sonuc=max_val(*liste)
print(sonuc)
