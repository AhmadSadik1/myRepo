def mygenerator():
    yield 1
    yield 2
    yield 3
    yield 4


gen = mygenerator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def myreutrn(n):
    reuslt = []
    for i in n:
        reuslt.append(i**3)
    return reuslt

myre = myreutrn([1 ,2 ,3 ,4 ,5])
print(myre)