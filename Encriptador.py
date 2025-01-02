import os
import pyaes

## abrir o arquivo a ser criptografado

file_name = "c:\\users\\igor.morais\\downloads\\teste.txt"
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover o arquivo original
os.remove(file_name)

## definir a chave de encriptacao

key =b"testecripto"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado

new_file = file_name+ ".criptografado"
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
