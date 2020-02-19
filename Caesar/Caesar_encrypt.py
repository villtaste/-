import  re

isrepeat = True
while isrepeat:
    input_text = input("アルファベットで暗号化したい文言を入れてね").lower()
    pattern = "[a-zA-Z]+"
    repatter = re.compile(pattern)
    if repatter.fullmatch(input_text):
        isrepeat = False
    else:
        print("アルファベットだけ入力してね")

input_key = int(input("キーにしたい数字を入れてね"))

def encrypter():
    encrypted_text = ""
    for i in input_text:
        added_ascii_cord = ord(i) + input_key
        if added_ascii_cord > 122:
            fixed_added_ascii_cord = added_ascii_cord - 26
            encrypted_text += chr(fixed_added_ascii_cord)
        else:
            encrypted_text += chr(added_ascii_cord)
    return encrypted_text

print(encrypter().upper())
