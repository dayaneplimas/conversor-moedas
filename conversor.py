def mostrar_menu():
    print("=== Conversor de Moedas ===")
    print("1 - Real para Dólar")
    print("2 - Real para Euro")
    print("3 - Dólar para Real")
    print("4 - Euro para Real")
    print("0 - Sair")

def converter(valor, taxa):
    return valor * taxa

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        print("Encerrando o conversor.")
        break

    if escolha in ["1", "2", "3", "4"]:
        valor = float(input("Digite o valor: R$ "))

        if escolha == "1":
            print(f"Dólar: US$ {converter(valor, 0.19):.2f}")
        elif escolha == "2":
            print(f"Euro: € {converter(valor, 0.16):.2f}")
        elif escolha == "3":
            print(f"Real: R$ {converter(valor, 5.3):.2f}")
        elif escolha == "4":
            print(f"Real: R$ {converter(valor, 6.2):.2f}")
    else:
        print("Opção inválida. Tente novamente.")
