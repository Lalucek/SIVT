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