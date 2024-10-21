def ingresar_puntuacion():
    while True:
        point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
        if point.isdecimal() and 1 <= int(point) <= 5:
            comment = input('Por favor, introduzca un comentario: ')
            with open("data.txt", 'a') as file_pc:
                file_pc.write(f'punto: {point} comentario: {comment}\n')
            break
        else:
            print('Por favor, introduzca un valor entre el 1 y 5')

def comprobar_resultados():
    try:
        with open("data.txt", "r") as read_file:
            print('Resultados hasta la fecha:\n' + read_file.read())
    except FileNotFoundError:
        print('No se encontraron resultados previos.')

def main():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

if __name__ == "__main__":
    main()
