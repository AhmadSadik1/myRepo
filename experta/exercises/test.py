from experta import *

class Greeting(KnowledgeEngine):
    @Rule()
    def greet(self):
        print("Hello, world!")

engine = Greeting()
engine.reset()
engine.run()