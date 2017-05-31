class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def reverseParentheses(b):
    new = []
    rt = ''
    s = Stack()
    for i in range(len(b)):
        if b[i] != ')':
            s.push(b[i])
        print s.size()
        print "#####"
        if b[i] == ')':
            t = ''
            while t != '(':
                t = s.pop()
                print t
                print "$$$$"
                if t == '(':
                    break
                else:
                    new.append(t)
            print "******"
            for a in new:
                print a
                s.push(a)
    for sz in range(s.size()):
        rt += s.pop()
    return rt[::-1]


test = 'a(bc)de'
print reverseParentheses(test)
