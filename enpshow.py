from encp import Calculate as cl
class Show:
    def showcalculator(self):
        first=int(input("Enter first number--"))
        second=int(input("Enter second number--"))
        third=int(input("Enter third number--"))
        four=int(input("Enter four number--"))
        cp=cl()
        cpvalue = cp.Sum(first,second,third,four)
        print("the sum is--", cpvalue)
        cpvalue1 = cp.Mul(first, second, third, four)
        print("the multiplication is--", cpvalue1)
        cpvalue2 = cp.Sub(first, second, third, four)
        print("The subtraction is--", cpvalue2)
display=Show()
display.showcalculator()
