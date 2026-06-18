def divBy13(num):
    # Converting a string into an integer
    num=int(num)
    # Check if the number is divisible by 13
    return num % 13 == 0
if __name__=="__main__":
    num="2910919"
    isDivisible=divBy13(num)
    if isDivisible:
        print("True")
    else:
        print("False")