def module(string):
        switcher = {
            '1006':'Maths',
            '1007':'OS',
            '1008':'DSA',
            '1009':'Object Oriented Programming',
            '1010':'Networking'
        }
        return switcher.get(string,"invalid module code")

string = str(input("Enter module code: "))
print(module(string))


for x in range(102,66,-1):
    if x != 0:
        print("the value of x is ",x)