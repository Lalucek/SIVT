class App:
    def __init__(self):
        self.vstup = self.ChcekInput(input("Napište číslo: "))
        self.PrevedNaZlomek(self.vstup)

    def ChcekInput(self, vstup):
        #TODO: Add input check
           return float(vstup)
    def gcd(self,x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    def PrevedNaZlomek(self,vstup):
         if(self.jeCeleCislo(vstup)):
            self.vysledek += str(vstup) + "/1" 
         else:
            print("Číslo má desetinná místa")
            citatel = vstup
            jmenovatel = 1
            while(self.jeCeleCislo(citatel) == False):
                citatel *= 10
                jmenovatel *= 10
            gcdnum = self.gcd(citatel, jmenovatel)
            print("GCD: " + str(gcdnum))
            citatel /= gcdnum
            jmenovatel /= gcdnum
            celecislo = citatel
            while(citatel > jmenovatel):
                celecislo += 1
                citatel -= jmenovatel
            print("Výsledek: " +str(int(celecislo)) + " a " + str(int(citatel)) + " / " + str(int(jmenovatel)))
            
    def jeCeleCislo(self,cislo):
        if(cislo - int(cislo) == 0):
            return True
        else:
            return False

pokracovat = "ANO"
while(pokracovat.upper == "ANO"):
    a = App()
    pokracovat = input("Chcete převést další číslo ? ANO/NE")
