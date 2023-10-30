from experta import *


class s(Fact):
    name = Field(bool)


class ScreenRule(KnowledgeEngine):
    @DefFacts()
    def userinput(self):
        yield s(name = False)
        yield Fact(isScreenON=input("Is Screen Turn On ? y|n:"))

    @Rule(Fact(isScreenON=L("n")))
    def isScreenONdef(self):
        
        print("Check Power Cable")

    @Rule(Fact(isScreenON=L("y")))
    def isScreenONdeT(self):
        self.declare(Fact(isScreenBlack=input("The Screen Is Black? y|n:")))

    @Rule(Fact(isScreenBlack=L("y")))
    def isScreenBlackdeT(self):
        print("Check Screen Card")

    @Rule(Fact(isScreenBlack=L("n")))
    def isScreenBlackdeF(self):
        self.declare(Fact(isOSOpened=input(" Is Operation System Opened? y|n:")))

    @Rule(Fact(isOSOpened=L("y")))
    def isOSOpeneddeT(self):
        self.declare(Fact(isPCAppared=input(" Is Desktop Appeared? y|n:")))

    @Rule(Fact(isPCAppared=L("n")))
    def isOSOpeneddeF(self):
        print("Press Ctrl Alt Del And Run Explorer.exe")

    @Rule(Fact(isPCAppared=L("y")))
    def isPCAppareddeT(self):
        print("System Health Is Good")

    @Rule(Fact(isOSOpened=L("n")))
    def isPCAppareddeF(self):
        self.declare(Fact(CanOpenSafe=input(" Can You Open Safe Mode? y|n:")))

    @Rule(Fact(CanOpenSafe=L("n")))
    def CanOpenSafedeF(self):
        print("Check Hard Disk Or Replace It")

    @Rule(Fact(CanOpenSafe=L("y")))
    def CanOpenSafedeT(self):
        self.declare(
            Fact(CanCheckHeath=input(" Can You Open Check System Health? y|n:"))
        )

    @Rule(Fact(CanCheckHeath=L("y")))
    def CanCheckHeathdeT(self):
        print("Continue With Process To Repair The System")

    @Rule(Fact(CanCheckHeath=L("n")))
    def CanCheckHeathdeF(self):
        print("Format The System")


engine = ScreenRule()
engine.reset()
engine.run()
