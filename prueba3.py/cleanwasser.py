#aaaaaa
import funcionesapp

ListaDpedidos=[]
while True:
    print("Bienvenido a Clean Wasser")
    print("1.Registrar pedido")
    print("2.Lista de los pedidos")
    print("3.Imprimir hoja de ruta")
    print("4.Buscar pedido por ID")
    print("5.Salir del programa")

    opc=int(input("Selccione una opcion: "))

    if opc == 1:
        funcionesapp.registrar_pedido(ListaDpedidos)
        print()
    elif opc == 2:
        funcionesapp.lista_pedidos(ListaDpedidos)
        ListaDpedidos.append
    elif opc == 3:
        funcionesapp.imprimir_hoja(ListaDpedidos)
        print()
    elif opc == 4:
        funcionesapp.buscar_pedido_ID(ListaDpedidos)
        print()
    elif opc == 5:
        print("Saliendo del programa")
    else:
        print("Ipcion no valida")