"""Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"
 """
def rank():
    if saldo(vit,derr) < 10:
        return "Ferro"
    elif 10< saldo(vit,derr) <=20:
        return "Bronze"
    elif 20< saldo(vit,derr) <=50:
        return "Prata"
    elif 50< saldo(vit,derr) <=80:
        return "Ouro"
    elif 80< saldo(vit,derr) <=90:
        return "Diamante"
    elif 90< saldo(vit,derr) <=100:
        return "Lendário"
    if saldo(vit,derr) > 100:
        return "Imortal"
 
    
def saldo(x,y):
    return x - y

while True:
    vit = int(input("Quantas vitorias você possui? "))
    derr = int(input("Quantas derrotas você possui? "))
    print(f"O Heroi tem saldo de {saldo(vit,derr)} e está no nivel de {rank()}")
    resp = str(input("Quer adicionar outro personagem? [S/N] ")).strip()
    if resp[0] not in 'Nn' :
        continue
        
    else:
        break
    