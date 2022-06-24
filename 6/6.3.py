

class Worker:
    name = "none"
    surname = "none"
    position = "none"

    __income = {"wage" : 0, "bonus": 0}

class Position(Worker):
    def get_total_income(self):
        return self._Worker__income.get("wage")+self._Worker__income.get("bonus")

    def set_position_wage(self, wage):
        self._Worker__income["wage"] = wage

    def set_position_bonus(self, bonus):
        self._Worker__income["bonus"] = bonus

w1 = Position()
w1.name = "aaa"
w1.surname = "bbb"
w1.position = "ccc"
w1.set_position_wage(40000)
w1.set_position_bonus(12000)

print(w1.get_total_income())
