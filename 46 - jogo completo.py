def criar_tabuleiro(): 
    return [["-" for _ in range(3)] for _ in range(3)]

def imprimir(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
    print()

def jogada(tabuleiro, linha, coluna, simbolo):
    if 0 <= linha <= 2 and 0 <= coluna <= 2:
        if tabuleiro[linha][coluna] == "-":
            tabuleiro[linha][coluna] = simbolo
            return True
    return False

def alterar_jogada(simbolo_atual):
    return "o" if simbolo_atual == "x" else "x"
    
def verificar_empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == "-":
                return False
    return True

def pontuacao(tabuleiro, simbolo):
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return True
    
    for j in range(3):
        if tabuleiro[0][j] == simbolo and tabuleiro[1][j] == simbolo and tabuleiro[2][j] == simbolo:
            return True
    
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        return True
    
    elif tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        return True
    
    return False

def placar1 (jogador1,jogador2, placar):

        print("\nPlacar:")
        print(f"{jogador1}: {placar[jogador1]}")
        print(f"{jogador2}: {placar[jogador2]}")


def main():   
    jogador1 = input("Digite seu nome (X): ")
    jogador2 = input("Digite seu nome (O): ")
    placar = {jogador1: 0, jogador2: 0}

    while True:
        tabuleiro = criar_tabuleiro()
        simbolo = "x"
        vencedor = ""

        while True:
            
            imprimir(tabuleiro)
            print(f"Vez do jogador {simbolo}")
            
            linha = int(input("Digite a linha (0-2): "))
            coluna = int(input("Digite a coluna (0-2): "))
        
            if jogada(tabuleiro, linha, coluna, simbolo):
                if pontuacao(tabuleiro, simbolo):
                    if simbolo == "x":
                        vencedor = jogador1
                        placar[vencedor] += 1 

                    else:
                        vencedor = jogador2
                        placar[vencedor] += 1

                    print(f"Parabéns jogador:, {vencedor}! Você venceu!")
                    imprimir(tabuleiro)
                    

                    break
                
                if verificar_empate(tabuleiro):
                    print("Empate! Todas as jogadas foram feitas.")
                    
                    break

                simbolo = alterar_jogada(simbolo)
            else:
                print("Jogada inválida ou local já ocupado. Tente novamente.")

        placar1(jogador1,jogador2,placar)
        
        continuar = input("Deseja jogar novamente? (s/n): ")
        if continuar != "s":
            print("Obrigado por jogar!")
            print("<<=====placar final=====>> ")
            placar1(jogador1,jogador2,placar)
            break

if __name__ == "__main__":
    main()
