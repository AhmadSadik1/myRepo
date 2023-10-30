from experta import *


class ScreenFact(Fact):
    isScreenON = Field(bool)
    isScreenBlack = Field(bool)
    isOSOpened = Field(bool)
    isPCAppared = Field(bool)
    CanOpenSafe = Field(bool)
    CanCheckHeath = Field(bool)


class ScreenRule(KnowledgeEngine):
    @DefFacts()
    def userinput(self):
        yield Fact(isScreenON=input('is screen turn on ? [y/n]:') == 'y')
           # self.declare(Fact(Screen_Turn_On=input('is screen turn on ? [y/n]:') == 'y'))
            #isScreenON= self.declare(bool(isScreenON =input("black True False : "))),
            # isScreenON= bool(input("black True False : ")),
            # isScreenON= bool(input("black True False : ")),
            # isScreenON= bool(input("black True False : ")),
            # isScreenON= bool(input("black True False : ")),
            # isScreenON= bool(input("black True False : "))
            # isScreenON= True
            # isScreenBlack=False,
            # isOSOpened=False,
            # CanOpenSafe=True,
            # CanCheckHeath=True,)

    @Rule(ScreenFact(isScreenON=L(False)), salience=11)
    def isScreenONdef(self):
        print("Check Power Cable")


    @Rule(ScreenFact(isScreenON=L(True)), salience=12)
    def isScreenONdeT(self):
        print("Is Screen Black")

    @Rule(ScreenFact(isScreenON=L(False)), salience=11)
    def isScreenONdef(self):
        print("Check Power Cable")

    @Rule(
        ScreenFact(isScreenON=L(True)) & ScreenFact(isScreenBlack=L(True)), salience=10
    )
    def isScreenBlackdeT(self):
        print("Check Screen Card")

    @Rule(
        ScreenFact(isScreenON=L(True)) & ScreenFact(isScreenBlack=L(False)), salience=9
    )
    def isScreenBlackdeF(self):
        print("Is Operating System Opened")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(True)),
        salience=8,
    )
    def isOSOpeneddeT(self):
        print("Is Desktop Appared")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(False)),
        salience=7,
    )
    def isOSOpeneddeF(self):
        print("Can You Open Safe Mode")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(True))
        & ScreenFact(isPCAppared=L(True)),
        salience=6,
    )
    def isPCAppareddeT(self):
        print("System Health Is Good")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(True))
        & ScreenFact(isPCAppared=L(False)),
        salience=5,
    )
    def isPCAppareddeF(self):
        print("Press Ctl Alt Del And Run Explorer.exe")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(False))
        & ScreenFact(CanOpenSafe=L(True)),
        salience=4,
    )
    def CanOpenSafedeT(self):
        print("Can You Check System Health")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(False))
        & ScreenFact(CanOpenSafe=L(False)),
        salience=3,
    )
    def CanOpenSafedeF(self):
        print("Check Hard Disk Or Replace It")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(False))
        & ScreenFact(CanOpenSafe=L(True))
        & ScreenFact(CanCheckHeath=L(True)),
        salience=2,
    )
    def CanCheckHeathdeT(self):
        print("Continue With Process To Repair The System")

    @Rule(
        ScreenFact(isScreenON=L(True))
        & ScreenFact(isScreenBlack=L(False))
        & ScreenFact(isOSOpened=L(False))
        & ScreenFact(CanOpenSafe=L(True))
        & ScreenFact(CanCheckHeath=L(False)),
        salience=1,
    )
    def CanCheckHeathdeF(self):
        print("Format The System")


engine = ScreenRule()
engine.reset()
engine.run()
