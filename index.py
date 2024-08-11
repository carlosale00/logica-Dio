while True:

    nome = input("nome do herio: ")
    xp = int(input("xp do heroi: "))

    if xp < 1_000:
        nivel = "Ferro"
    elif xp > 1_000 and xp <= 2_000:
        nivel = "Bronze"
    elif xp > 2_000 and xp <= 3_000:
        nivel = "Prata"
    elif xp > 3_000 and xp <= 4_000:
        nivel = "Ouro"
    elif xp > 5_000 and xp <= 6_000:
        nivel = "Platina"
    elif xp > 6_000 and xp <= 7_000:
        nivel = "Diamante"
    elif xp > 8_000 and xp <= 9_000:
        nivel = "Ascendente"
    elif xp > 9_000 and xp <= 10_000:
        nivel = "Imortal"
    elif xp > 10_000:
        nivel = "Radiante"

    print(f"\nO Heroi de nome {nome} está no nivel {nivel}\n")

    sair = int(input("deseja Sair ? sim = 0 , não = 1: "))
    print()

    if sair == 0:
        print("Programa Finalizado")
        break
