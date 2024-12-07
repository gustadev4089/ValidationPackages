import re # regular expression package imported

regions = { # Dictionary containing acronyms of brazilian states and their respective codes
    '0': ['RS'],
    '1': ['DF','GO','MS','MT','TO'],
    '2': ['AC','AM','AP','PA','RO','RR'],
    '3': ['CE','MA','PI'],
    '4': ['AL','PB','PE','RN'],
    '5': ['BA','SE'],
    '6': ['MG'],
    '7': ['ES','RJ'],
    '8': ['SP'],
    '9': ['PR','SC']
}

def check_digit(cpf): # function that check (CPF) digits
    new_cpf = str('')
    soma = int(0)
    for i, c in enumerate(range(10,1,-1)):
        soma += int(cpf[i])*int(c)
    
    if soma%11 == 0 or soma%11 == 1:
        new_cpf = cpf[0:9]+'0'
    else:
        r = 11-(soma%11) 
        new_cpf = cpf[0:9]+str(r)

    soma = int(0)
    for i, c in enumerate(range(10,1,-1)):
        soma += int(new_cpf[i+1])*int(c)
    
    if soma%11 == 0 or soma%11 == 1:
        new_cpf = new_cpf+'0'
    else:
        r = 11-(soma%11) 
        new_cpf = new_cpf+str(r)
    
    if(new_cpf == cpf):
        return True
    else:
        return False

def check_is_format_cpf(cpf) -> str or bool :
    validate1 = re.compile(r'[0-9]{11}') # regular expression for just numbers
    validate2 = re.compile(r'(?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2}') # regular expression with dots

    number = str('')

    if(validate1.search(cpf) != None): # case format without dots
        number = (validate1.search(cpf).group())
    else:
        if(validate2.search(cpf) != None): # case format with dots
            number = (validate2.search(cpf).group())
        else:
            return False # case format invalid
    
    number = (re.sub(r'\D', r'', number)) # cleaning the regular expression
    return number

class Cpf: # class that return if content is valid
    def __init__(self, content) -> None:
        self.content = content
        return None

    def cpf_is_valid(self: str) -> bool:
        try:
            self.content.isnumeric() # verify if all content is digit
            number = check_is_format_cpf(self.content)
            return check_digit(number)

        except: # case content don't digit
            return False
    
    def cpf_region(self: str) -> list:
        try:
            self.content.isnumeric() # verify if all content is digit
            number = check_is_format_cpf(self.content)
            if check_digit(number):
                return regions[number[8]]
            
        except: # case content don't digit
            return []
