# def avm(fun):
#     def wrapper(Student_name, math_mark, ExpertSystem_mark, Programing_mark):
#         ave_mark = (math_mark + ExpertSystem_mark + Programing_mark) / 3.0
#         return fun(Student_name, ave_mark)
#     return wrapper

# @avm
# def info(Student_name, ave_mark):
#     Sinfo = {'name': Student_name,
#              'M_mark': math_mark, 'EX_m': ExpertSystem_mark,
#              'P_mark': Programing_mark}
#     print(Sinfo)
#     print(ave_mark)

# info('soso', 80, 75, 90)
# avg_mark = 0


# def info(fun):
#     def marks(Student_name, math_mark, ExpertSystem_mark, programming_mark):
#         avg_mark = (math_mark + ExpertSystem_mark + programming_mark) / 3
#         return fun(Student_name, avg_mark)
#     return marks


# @info
# def nameavg(Student_name, math_mark, ExpertSystem_mark, programming_mark):
#     avg_mark = (math_mark + ExpertSystem_mark + programming_mark) / 3
#     print(Student_name , avg_mark)

# nameavg('ahmad' , 90 , 90 , 90)


# def pr(name , mark) :
#     news = {'names' : name , 'mark' : mark}
#     print(news)

# pr('ahmad' , 30)







def full(fun):
    def nesteddeocr(name, math_mark, expertsystem_mark, programming_mark):
        print(f"student reuslt {name}")
        fun(name, math_mark, expertsystem_mark, programming_mark)
    return nesteddeocr


@full
def sm(name, math_mark, expertsystem_mark, programming_mark):
    newsm = {'names': name, 'math_marks': math_mark, 'expertsystems':
             expertsystem_mark, 'programming_marks': programming_mark}
    avg = (math_mark + expertsystem_mark + programming_mark)/3
    reuslt = {'student_name': name, 'avg_mark ': avg}
    print([key for key in reuslt.values()])

    # print(reuslt)
sm('ahmad' , 30 ,30 ,30 )