import re

isrepeat = True
while isrepeat:
    input_text = input("復号化したいアルファベットをいれてね").lower()
    pattern = "[a-zA-Z]+"
    repatter = re.compile(pattern)
    if repatter.fullmatch(input_text):
        isrepeat = False
    else:
        print("アルファベットだけ入力してね")

input_key = int(input("キーの数字を入れてね"))

def decrypter():
    decrypted_text = ""
    for i in input_text:
        decreased_ascii_cord = ord(i) - input_key
        if decreased_ascii_cord < 97:
            fixed_decreased_ascii_cord = decreased_ascii_cord + 26
            decrypted_text += chr(fixed_decreased_ascii_cord)
        else:
            decrypted_text += chr(decreased_ascii_cord)
    return decrypted_text

print(decrypter().lower())