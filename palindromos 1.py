def run():
    palabra = str(input("Escribe una palabra: ")).lower().replace(' ', '')
    if palabra[::] == palabra[::-1]:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()