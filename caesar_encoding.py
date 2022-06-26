# Итак, нужно написать функцию, которая будет видоизменять входную строку шифром Цезаря со сдвигом.  (Каждая буква в подаваемой строке меняется на следующую по алфавиту, либо на предыдущую в зависимости от направления кодирования)

# !! Например при сдвиге вперед (С1) - из слова "Hello" получается слово "Ifmmp".
# При сдвиге назад (С0) -  слово "Hello" превратится в "Gdkkn"

# На вход функции подается строка и последовательность кодирования/декодирования.

# Например: Caesar("hello", "C1-C0-C1-C0") вернет нам "hello", т.к. мы дважды смещали вперед (кодировали), и дважды смещали назад (декодировали):)
    
def direction(sentence):
    arr = sentence.split('-')
    count = 0
    for i in arr:
        if i == "C1":
            count += 1
        elif i == "C0":
            count -= 1
    return count

def Caesar(text, shift):
    number = direction(shift)
    cipher = ''
    error = "not supported value by ASCII"   
    for char in text:
        if not char.isalpha():
            flag = char
        elif char.isupper():
            code = ord(char) + number
            if 64 < code <= 90:
                flag = chr(code)
            elif code > 90:
                flag = chr((code - 90) + 64)
            elif code <= 64:
                flag = chr((code + 90) - 64)           
        elif char.islower():
            code = ord(char) + number
            if 96 < code <= 122:
                flag = chr(code)
            elif code > 122:
                flag = chr((code - 122) + 96)
            elif code <= 96:
                flag = chr((code + 122) - 96)       
        else:
            return error        
        cipher += flag 
    return cipher

test = "CHEtamA"
num = "C0-C0-C1-C1-C0-C0-C0"

print(Caesar(test, num))
