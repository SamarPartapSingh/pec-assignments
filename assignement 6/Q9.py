class Parentheses:
    def is_valid(self,string):
        valid = True
        stack = []

        for i in string:
            if i in ['(','{','[']:
                stack.append(i)
            elif i in [')','}',']']:
                if len(stack) == 0:
                    valid = False
                    break
                else:
                    top = stack.pop()
                    if i == ')' and top != '(':
                        valid = False
                        break
                    elif i == '}' and top != '{':
                        valid = False
                        break
                    elif i == ']' and top != '[':
                        valid = False
                        break

        if len(stack) != 0:
            valid = False

        return valid


string = "(){}[]"
result = Parentheses().is_valid(string)
print(result)