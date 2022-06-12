winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
fall = [9,10,11]
year = [winter,spring,summer,fall]

m = input("enter m_number")
for b in year:
    if m in(b):
        print(b.index)
