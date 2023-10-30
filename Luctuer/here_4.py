from experta import *


class player (Fact):
    name = Field(str)
    age = Field(int)


class weather(Fact):
    tempdeg = Field(float)
    israinny = Field(bool)


class engine(KnowledgeEngine):
    # @DefFacts(player)
    @Rule(player(age=P(lambda age: age < 18)))
    def p_age(self):
        print("ينصح بقضاء العطلة بقراءة القصص القصير ة الانكليزية، أو حل الألغاز")

    @Rule(player(age=P(lambda age: age > 18)))
    def W_age(self):
        self.declare(weather(tempdeg = 15 , israinny = False))

    @Rule(weather(tempdeg=P(lambda tempdeg: tempdeg > 11) &
                  P(lambda tempdeg: tempdeg < 19)) & weather(israinny = P(lambda israinny : israinny == False)))
    def tem (self) :
        print("ينصح بقضاء العطلة في المتحف الوطني ")
    
    @Rule(weather(israinny = False))
    def lib (self) :
        print("ينصح بقضاء العطلة في مكتبة الاسد")

if __name__ == '__main__'   :
    engine = engine()
    players = player(name="Ahmed", age=15)
    engine.reset()
    engine.declare(players)
    engine.run()






















# class Player(Fact):
#     name = Field(str, mandatory=True)
#     age = Field(int, mandatory=True)
# # تعريف قاعدة Rule
# @Rule(Player(age=P(lambda age: age < 18)))
# def underage_player(player):
#     print("ينصح بقضاء العطلة بقراءة القصص القصيرة الانكليزية، أو حل الألغاز.")
# # تعريف محرك المعرفة
# # تشغيل محرك المعرفة وتمرير اللاعب إليه
