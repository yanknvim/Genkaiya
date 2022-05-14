import sys

stack = []

f = open(sys.argv[1]) # open file
code = f.read()
f.close()

words = code.split()

for word in words:
    if (not '限' in word) and (not '界' in word) and (not 'や' in word): #push num
        value = word.replace('!','1').replace('?','0')
        value = int(value, 2)
        stack.append(value)
    elif word == "限": #Add
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif word == "界": #Minus
        a = stack.pop()
        b = stack.pop()
        stack.append(b - a)
    elif word == "限限": #Multi
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif word == "限界": #Divide
        a = stack.pop()
        b = stack.pop()
        stack.append(b / a)
    elif word == "や": #print
        value = stack.pop()
        print(chr(value),end="")
    elif word == "やや": #read
        stack.append(int(input()))
