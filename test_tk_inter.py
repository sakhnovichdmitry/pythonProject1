class Purse:
    def __init__(self, valuta, name='Inkognito'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        print('Пополнение', self.name, 'на:', howmany)
        return howmany

    def top_down_balance(self, howmany):
        if self.__money - howmany < 0:
            print('Недостаточно срадств')
            raise ValueError('Не достаточно средств')
        self.__money = self.__money - howmany
        print('Списание', self.name, 'на:', howmany)
        return howmany


    def info(self):
        print (self.name, self.__money, self.valuta)

    def __del__(self):
        print('Кошелек', self.name, 'удален')



x = Purse('USD', 'Larry')
y = Purse('USD', 'Barry')
x.info()
y.info()
y.top_up_balance(10)
x.top_up_balance(y.top_down_balance(7))
x.info()
y.info()
