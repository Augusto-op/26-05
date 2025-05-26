distancia_percorrida = float(input("Digite a distancia percorrida em km "))
combustivel_gasto = float(input("Digite a quantidade de combustivel gastos em livros "))

consumo_medio = distancia_percorrida / combustivel_gasto

match consumo_medio:
    case valor if valor < 8:
        print("consumo menor que 8 km/1 - DESEMPENHO RUIM")
    case valor if valor < 12:
        print ("Consumo entre 8 e 12 km/1 - DESEMPENHO MEDIO")
    case _:
        print("Consumo maior ou igual a 12 km/1 - OTIMO DESEMPENHO")