# from experta import *


# class Fact(Fact):
#   pass


# class Player(Fact):

#   name = Field(str)
#   age = Field(int)


# class Weather(Fact):
#   tempdeg = Field(float)
#   israiny = Field(bool)


# class HolidayRecommendationRules(KnowledgeEngine):
   
#    @DefFacts()
#    def players(self):
#     yield Player(name="Loky", age=25)

#   @Rule(Player(age=P(lambda x: x < 18)))
#   def recommend_reading(self):
#     print("ينصح بقضاء العطلة بقراءة القصص القصيرة الانكليزية ،او حل الالغاز")
#   @Rule(Player(age=P(lambda x: x >= 18)))
#   def generate_weather_fact(self):
#     self.declare(Weather(tempdeg=15.0, israiny=False))

#   @Rule(Weather(tempdeg=P(lambda tempdeg: tempdeg > 11) &
#                   P(lambda tempdeg: tempdeg < 19)) & Weather(israinny = P(lambda israinny : israinny == False)))
#   def tem (self) :
#     print("ينصح بقضاء العطلة في المتحف الوطني ")

#   @Rule(Weather(israiny=False))
#   def recommend_library(self):
#     print("ينصح بقضاء العطلة في مكتبة الأسد")

# if name =='main':
#     engine = HolidayRecommendationRules()
#     players = Player(name="mayas", age=15)
#     engine.reset()
#     engine.declare(players)
#     engine.run()