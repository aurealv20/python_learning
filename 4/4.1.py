from sys import argv
script_name, hhrs, hrph, hbonus = argv

def salary(hrs, RpH, bonus = 0):
    return (hrs*RpH)+int(bonus)

sl = salary(float(hhrs), int(hrph), int(hbonus))
if sl == 0:
    print("выдать пиздюлей")
else:
    print(f"выдать {sl} рублей")

