from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def validate_brackets(string):
    """
    function called validate brackets with Arguments: string and Return: boolean
    
    this function representing whether or not the brackets in the string are balanced
    
    """
    stack = Stack()
    for ch in string:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(validate_brackets( "()" ))
    print(validate_brackets("))((a+b}{"))
    print(validate_brackets("((a+b))"))
    print(validate_brackets("((a+g))"))
    print(validate_brackets("))"))
    print(validate_brackets("[a+b]*(x+2y)*{gg+kk}"))