def palindromo(palabra):
    if palabra == palabra[::-1]: return True
    else: return False


def main():
    palabra = str(input('Ingresar palabra:\n')).replace(' ', '').lower()
    if palindromo(palabra): print('palindromo')
    else: print("palindromon't")


while 1:

    if __name__ == "__main__": main()