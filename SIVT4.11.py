zavorky = input()
def Valid(text):
    oteviraci = []
    uzaviraci = []
    for i in text:
        if (i == "("):
            oteviraci.append(i)
        else:
            uzaviraci.append(i)
    if(len(oteviraci) == len(uzaviraci)):
        return True
    else:
        return False

print(Valid(zavorky))

def Valid2(text):
    zavorky = []
    for i in text:
        print(i)
        if(i == '('):
            zavorky.append(i)
        else:
            if(len(zavorky) == 0):
                return False;
            else:
                zavorky.pop()
                print(text)
    if(len(zavorky) == 0):
        return True
    else:
        return False

print(Valid2(zavorky))