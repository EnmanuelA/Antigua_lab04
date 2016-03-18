def simpleExpressionIsValid(expr):
        isValid = True;

        # s must contain an operator
        plus_sign = expr.find("+")
        minus_sign = expr.find("-")
        mult_sign = expr.find("*")
        div_sign = expr.find("/")
        all_signs = max(plus_sign,minus_sign,mult_sign,div_sign)
        if all_signs == -1:
            isValid = False
        # so far so good (we have an operator)
        else:
            # check if we have numbers on either sides of operator
            num1Str = expr[:all_signs]
            num2Str = expr[all_signs+1:]
            isValid = num1Str.isnumeric() and num2Str.isnumeric()

        return isValid

def evaluateSimpleExpression(expr):
        plus_sign = expr.find("+")
        minus_sign = expr.find("-")
        mult_sign = expr.find("*")
        div_sign = expr.find("/")
        all_signs = max(plus_sign,minus_sign,mult_sign,div_sign)

        num1 = int(expr[:all_signs])
        num2 = int(expr[all_signs+1:])
        if all_signs == minus_sign:
            val = num1 - num2
        elif all_signs == plus_sign:
            val = num1 + num2
        elif all_signs == mult_sign:
            val = num1 * num2
        else: # if all_signs == div_sign:
            val = num1 / num2
        return val


def evaluateTerm (expr):
        return evaluateSimpleExpression(expr[1:len(expr)-1])

def termIsValid (expr):
        isValid = True

        if expr [0] != "(" or expr [len(expr)-1] != ")":
            isValid = False
        else:
            isValid = simpleExpressionIsValid(expr[1:len(expr)-1])
        return isValid


def complexExpressionIsValid (expr):
    isValid = True
    expr = expr.replace(" ", "")
    keepGoing = True
    while keepGoing:
        mult_sign = expr.find("*")
        if mult_sign !=-1:
            term = expr[:mult_sign]
            expr = expr[mult_sign+1:]
            isValid = termIsValid(term)
            keepGoing = isValid
        else:
            isValid = termIsValid(expr)
            keepGoing = False
    
    return isValid

                            

def evaluateComplexExpression (expr):
    value = 1
    expr = expr.replace(" ", "")
    keepGoing = True
    while keepGoing:
        mult_sign = expr.find("*")
        if mult_sign !=-1:
            term = expr[:mult_sign]
            expr = expr[mult_sign+1:]
            value *= evaluateTerm(term)
        else:
            value *= evaluateTerm(expr)
            keepGoing = False
    
    return value

keepGoing = True
while keepGoing:
    expr =input("Please enter an expression with the form ""'number+number' or \"end\" to quit: ")
    if expr == "end":
      keepGoing = False

    else:

        if expr [0] == "(" and expr [len(expr)-1] == ")":
                expr = (expr[1:len(expr)-1])

        if simpleExpressionIsValid(expr) or evaluateTerm (expr):
            value = evaluateSimpleExpression(expr)
            print (expr + " = " + str(value))
        else:
            print ("Invalid expression")
print("Done.")



