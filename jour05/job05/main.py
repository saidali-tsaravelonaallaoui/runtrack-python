message_original = "Jules César"
decalage = 3

def chiffre_cesar(message, decalage):
    message_chiffre = ''
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            message_chiffre += chr((ord(char) - ascii_offset + decalage) % 26 + ascii_offset)
        else:
            message_chiffre += char
    return message_chiffre

message_chiffre = chiffre_cesar(message_original, decalage)

print(f"Message original : {message_original}")
print(f"Message chiffré : {message_chiffre}")