
#---------- CONSTANTS ----------#
PHYSICAL = 0
MAGICAL = 1
NORMAL = 2
POISON = 3
FIRE = 4





#---------- DAMAGE CLASS ----------#
class damage:
    def __init__(self, amount, kind):
        self.amount = amount
        self.type = kind