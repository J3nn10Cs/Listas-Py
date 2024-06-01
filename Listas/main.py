import os as o
List = []

def CreatList():
    o.system('cls')
    global List
    print('Crear una nueva tarea \n')
    lista = input('Ingrese una el nombre de la tarea : ')
    #agregar
    List.append(lista)
    # #Mostrar la lista
    # ShowList()

def ShowList():
    o.system('cls')
    print('\n**************************************************')
    for list in List:        
        #devuelve posición
        print(f'{List.index(list) + 1}. {list}')
    print('************************************************** \n')

def UpdateList():
    o.system('cls')
    global List
    print('********Actualizar***********\n')
    listid = int(input('Ingrese el ID a actualizar : '))
    List[listid - 1] = List[listid - 1] + '✅'
    print('Tarea Acrualizada')
    
def DeleteList():
    o.system('cls')
    global List
    print('*******+Eliminar Lista*********\n')
    listId = int(input('Ingrese el ID a eliminar : '))
    del List[listId - 1]
    print(f'Lista {listId} eliminada')

def main():
    print('.: Bienvenido a Python .: \n ')
    
    while True:
        options = int(input('\n 1)Crear una tardea \n 2) Mostrar tarea \n 3) Marcar realizada una tarea \n 4) Borrar una tarea \n 5) Salir \n Elija una opción : '))
        match options:
            case 1: 
                CreatList()
            case 2: 
                ShowList()
            case 3: 
                UpdateList()
            case 4: 
                DeleteList()
            case 5: 
                print('Hasta pronto')
                break
            case _: 
                print('Opción no valida')
                break
    
if __name__ == '__main__':
    main()
    
