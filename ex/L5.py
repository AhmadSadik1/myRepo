from experta import *


class Rcs(KnowledgeEngine):
    @DefFacts()
    def dignose(self):
        print('plase , answer the following question: ')
        yield Fact(action='start dignose')

    @Rule(Fact(action='start dignose'), NOT(Fact(scran=W())), salience=6)
    def rtnodel(self):
        self.declare(Fact(scren=input('its screen trun on n | y') , ))
        # self.declare(Fact(scren = input("its's screen turn on n | y") == 'y'))


    @Rule(Fact(scren = 'y' , color = 'black'))
    def printer(self):
        print("yasta cheeck here")
    
    @Rule(Fact(scren = 'n'))
    def pr (self):
        print('yasta power')


engine = Rcs()
engine.reset()
engine.run()




from experta import *


class player (Fact):
    name = Field(str)
    age = Field(int)

    
class weather(Fact):
  # it's not fact 
    tempdeg = Field(float)
    israinny = Field(bool)


class engine(KnowledgeEngine):
    @DefFacts()
    def players(self):
      yield player(name="Loky", age=25)


    @Rule(player(age=P(lambda age: age < 18)))
    def p_age(self):
        print("ينصح بقضاء العطلة بقراءة القصص القصير ة الانكليزية، أو حل الألغاز")

    @Rule(player(age=P(lambda age: age >= 18)))
    def W_age(self):
        self.declare(weather(tempdeg = 15.0 , israinny = False))

    @Rule(weather(tempdeg=P(lambda tempdeg: tempdeg >= 12) &
                  P(lambda tempdeg: tempdeg < 19)) & weather(israinny =L(False)))
    def tem (self) :
        print("ينصح بقضاء العطلة في المتحف الوطني ")
    
    @Rule(weather(israinny =L(False)))
    def lib (self) :
        print("ينصح بقضاء العطلة في مكتبة الاسد")



engine = engine()
# players = player(name="Ahmed", age=15)
# weatherp = weather(tempdeg = 13.4 , israinny = False)
engine.reset()
# engine.declare(weatherp)
engine.run()