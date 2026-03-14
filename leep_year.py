#find leep year or not

year = int(input("Enter a year "))

def checkyear(year):
    return (((year%4 ==0)and(year%100 !=0)) or (year%400 ==0))

if checkyear(year):
    print("leep year")
else:
    print("Not a leep year")
