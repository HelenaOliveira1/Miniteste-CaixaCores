import Cor


def main():
    print("Opção 1 - Adicionar Cor , Opção 2 - Listar Cor , Opção 3 - Encerrar Programa")
    op = int(input("Qual opção deseja usar? "))

    while (op != 3):
        if (op == 1):
            Cor.AdicionarCor()
            print("")
            print("Opção 1 - Adicionar Cor , Opção 2 - Listar Cor , Opção 3 - Encerrar Programa")
            op = int(input("Qual opção deseja usar? "))

        elif (op == 2):
            Cor.ListarCores(Cor.cor)
            print("")
            print("Opção 1 - Adicionar Cor , Opção 2 - Listar Cor , Opção 3 - Encerrar Programa")
            op = int(input("Qual opção deseja usar? "))

    if (op == 3):
        print("")
        print("Programa Encerrado.")

main()
