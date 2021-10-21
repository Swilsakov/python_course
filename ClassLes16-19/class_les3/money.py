#Dollar
'''
dollarize(123456.78901) -> "$123,456.80"
dollarize(-123456.7801) -> "-$123,456.78"
dollarize(1000000) -> "$1,000,000"
'''

# class Dollar:
#     def __init__(self, d1, d2, d3):
#         self.d1 = d1
#         self.d2 = d2
#         self.d3 = d3
    
#     def doll(self):
#         print(self.d1, self.d2, self.d3)
#         print(d1, '->', a1)
#         print(d2, '->', a2)
#         print(d3, '->', a3)

# d = Dollar()
# a1 = '${:,.2f}'.format(d1)
# a2 = '${:,.2f}'.format(d2)
# a3 = '${:,.2f}'.format(d3)
# s = Dollar()
# s.doll('123456.78901', '-123456.7801', '1000000')
# d.doll()

class MoneyFMT:
    def __init__(self, d1, d2, d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
   
    def update(self):
        return (self.d1, self.d2, self.d3)

    def __repr__(self):
        return f'Money - {d1} {d2} {d3}'.format(d1 = self.d1, d2 = self.d2, d3 =self.d3)

    def __str__(self):
        return(self.d1, self.d2, self.d3)
        return'${:,.2f}'.format(self.d1)
        return'${:,.2f}'.format(self.d2)
        return'${:,.2f}'.format(self.d3)


doll = MoneyFMT(123456.78901, -123456.7801, 1000000)
print(doll.update())