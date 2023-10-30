from experta import *


class Screen(Fact):
    Screen_Turn_On = Field(bool)
    Screen_Color_Black = Field(bool)
    Screen_Operation_System_Opened = Field(bool)
    Screen_Desktop_Appeared = Field(bool)
    Screen_Can_You_Open_Safe_Mode = Field(bool)
    Screen_Can_You_Open_Check_System_Health = Field(bool)


class RCS(KnowledgeEngine):
    @DefFacts()
    def diagnose(self):
        print('please, answer the following question:')
        yield Fact(action='start diagnose')

    @Rule(Fact(action='start diagnose'), NOT(Fact(Screen_Turn_On=W(), Screen_Color_Black=W())))
    def screen(self):
        self.declare(Fact(Screen_Turn_On=input('is screen turn on ? [y/n]:') == 'y'))
        self.declare(Fact(Screen_Color_Black=input('the screen is black? [y/n]:') == 'y'))

    @Rule(Fact(Screen_Turn_On=True, Screen_Color_Black=True))
    def scr_on(self):
        print('Check Screen card')

    @Rule(Fact(Screen_Turn_On=L(False)))
    def scr_off(self):
        print('Check power cable')

    @Rule(Fact(action='start diagnose'), (Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=W(), Screen_Desktop_Appeared=W())))
    def operating(self):
        self.declare(Fact(Screen_Operation_System_Opened=input(' is Operation_System_Opened? [y/n]:') == 'y'))
        self.declare(Fact(Screen_Desktop_Appeared=input(' is Desktop_Appeared? [y/n]:') == 'y'))

    @Rule(Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=True, Screen_Desktop_Appeared=True))
    def desktop_on(self):
        print('System Health is Good')

    @Rule(Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=True,
               Screen_Desktop_Appeared=False))
    def desktop_off(self):
        print('Press ctrl alt del and run explorer.exe')

    @Rule(Fact(action='start diagnose'), (Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=W(), Screen_Can_You_Open_Safe_Mode=W())))
    def Safe_Mode(self):
        self.declare(Fact(Screen_Can_You_Open_Safe_Mode=input(' Can_You_Open_Safe_Mode? [y/n]:') == 'y'))
        self.declare(Fact(Screen_Can_You_Open_Check_System_Health=input(' Can_You_Open_Check_System_Health? [y/n]:') == 'y'))

    @Rule(Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=False,
               Screen_Can_You_Open_Safe_Mode=False))
    def hard_disk(self):
        print('check Hard disk or replace it')

    @Rule(Fact(action='start diagnose'), (Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=True, Screen_Can_You_Open_Safe_Mode=True, Screen_Can_You_Open_Check_System_Health=W())))
    def hard_disk(self):
        self.declare(Fact(Screen_Can_You_Open_Check_System_Health=input(' Can_You_Open_Check_System_Health? [y/n]:') == 'y'))

    @Rule(Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=False,
               Screen_Can_You_Open_Safe_Mode=True, Screen_Can_You_Open_Check_System_Health=True))
    def check_system(self):
        print('Continue With Process to Repair the System')

    @Rule(Fact(Screen_Turn_On=True, Screen_Color_Black=False, Screen_Operation_System_Opened=False,
               Screen_Can_You_Open_Safe_Mode=True, Screen_Can_You_Open_Check_System_Health=False))
    def check_system_(self):
        print('Format The System')


engine = RCS()
engine.reset()
engine.run()