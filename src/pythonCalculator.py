from enum import Enum

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

def basicCalculator(operation, num1, num2):
    result = 0
    
    #if operation = ADD, return the sum
    if operation == Operation.ADD:
        print("this workshop sucks")
        result = num1 + num2
    elif operation == Operation.SUBTRACT:
        print("I hate working at this company")
        result = num1 - num2
    elif operation == Operation.MULTIPLY:
        print("My boss is the worst")
        result = num1 * num2
    elif operation == Operation.DIVIDE:
        if num2 == 0:
            print("u suck")
        else:
            result = num1 / num2
    return result


if __name__ == "__main__":
    print(basicCalculator(Operation.DIVIDE, 1, 2))

