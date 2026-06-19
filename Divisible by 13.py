#Approach#1: Native Approach
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

#Approach#2: Alternating Sum of 3-Digit Blocks
function divBy13(s) {
    let len = s.length;

    // Special case: if the number is "0"
    if (len === 1 && s[0] === '0') {
        return true;
    }

    // Make the length a multiple of 3 by padding zeros at the end
    if (len % 3 === 1) {
        s += "00";
        len += 2;
    } else if (len % 3 === 2) {
        s += "0";
        len += 1;
    }

    let sum = 0;
    let p = 1;

    // Traverse from right to left in steps of 3 digits
    for (let i = len - 1; i >= 0; i--) {
        let group = 0;
        group += parseInt(s[i--]);
        group += parseInt(s[i--]) * 10;
        group += parseInt(s[i]) * 100;

        sum += group * p;
        p *= -1;
    }

    sum = Math.abs(sum);
    return sum % 13 === 0;
}

// Driver Code
const s = "2911285";
console.log(divBy13(s));

#Approach#3: String-Based Modulo
function divBy13(s) {
    
    // Stores running remainder
    let rem = 0;  

    // Process each digit and compute remainder modulo 13
    for (let i = 0; i < s.length; i++) {
        rem = (rem * 10 + (s.charCodeAt(i) - '0'.charCodeAt(0))) % 13;
    }

    // Final check for divisibility
    return rem === 0;
}

// Driver Code
let s = "2911285";

if (divBy13(s))
    console.log("true");
else
    console.log("false");
