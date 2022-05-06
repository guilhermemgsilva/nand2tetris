def notMoreThanNumberOne(bit):
    if bit <= 1:
        return bit
    else:
        return 1

def andPort(input1, input2):
    return input1*input2

def orPort(input1, input2):
    return notMoreThanNumberOne(input1+input2)


     