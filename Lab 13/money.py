# money.py

class Money:

    def __init__(self):
        self.dollars = 0
        self.cents = 0

    def getDollars(self):
        return self.dollars

    def getCents(self):
        return self.cents

    def setDollars(self, dollars):
        if type(dollars) == int and dollars >= 0:
            self.dollars = dollars

    def setCents(self, cents):
        if type(cents) == int and cents >= 0:
            self.cents = cents
            if cents >= 100:
                self.cents = cents % 100
                self.dollars += (cents // 100)

    def __str__(self):
        myMoney = self.dollars + self.cents / 100
        rtnStr = "${0:0.2f}".format(myMoney)
        return rtnStr

    def compareTo(self, m):
        value = 0
        if self.dollars != m.getDollars():
            value = self.dollars - m.getDollars()
        elif self.cents != m.getCents():
            value = self.cents - m.getCents()
        return value

    def increment(self, m):
        self.setDollars(self.dollars + m.getDollars())
        self.setCents(self.cents + m.getCents())
 
