# def decr(fun):
#     def nesteddecr():
#         print("This first line ")
#         fun()
#         print("This last line ")

#     return nesteddecr


# @decr
# def names():
#     print("soos")


# names()


def pardec(fun):
    def nesteddeocr(num1, num2 , num3):
        if num1 < 0 or num2 < 0:
            print("Erorr")
        # fun(num1 , num2 ,num3)
    print("soso")
    return nesteddeocr



def cul(n1 ,n2 , n3):
    print (n1 + n2 + n3) 

cul(5 ,5 ,5)
