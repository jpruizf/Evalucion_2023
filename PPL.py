from gestor_fede import Gestor_Federado
from gestor_eval import Gestor_Evaluacion


def menu():
    print("1->Iniciar|0->Terminar")
    inicio=input("Selecione una de las opciones->")
    while inicio != '0':
        G_F=Gestor_Federado()
        G_E=Gestor_Evaluacion()
        print("a->Ver datos de los patinadores para un estilo->")
        print("b->Ver datos del patinador que mayor puntuacion obtuvo")
        print("c->Ver listado de patinador que participo con mas de un estilo")
        print("d->Ver la valoracion de los 3 jurados")
        opcion = input("Seleccione una de las opciones")
        if opcion == 'a':
            G_F.cargar_federado()
            G_F.cargar_puntaje()
            G_E.cargar_evaluacion()
            aux1 = input("Estilo->L:LIBRE|E:ESCUELA")
            code = G_E.buscar_estilo(aux1)
            G_F.mostrar_estilo(code)
        elif opcion == 'b':
            G_F.ordenar_puntaje()
        elif opcion == 'c':
            codex = G_E.buscar_mas_de_un_estilos()
            G_F.listado_mas_estilos(codex)
        elif opcion == 'd':
            dn_aux = int(input("DNI->"))
            G_F.mostrar_puntos(dn_aux)
if __name__ == '__main__':
    menu()