def caesarCipher(s, k):
    new_text = ''
    k = k % 26

    for caractere in s:
        if caractere.isalpha():
            is_upper = caractere.isupper()
            new_char = chr((ord(caractere.lower()) - ord('a') + k) % 26 + ord('a'))
            new_text += new_char.upper() if is_upper else new_char
        else:
            new_text += caractere

    print(new_text)
    return new_text

caesarCipher(s='criptografando-um-texto-qualquer', k=2)
caesarCipher(s='fnnfkd-hmsdquhdv', k=1)
caesarCipher(s='ban-áusz', k=4)