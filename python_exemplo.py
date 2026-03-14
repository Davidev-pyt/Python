def calcular_aluguel(modelo, dias):
    # Categorias de carros e seus respectivos modelos
    categorias = {
        "Luxo": ["Ferrari", "Lamborghini", "Porsche", "Tesla Model S"],
        "Premium": ["BMW", "Audi", "Mercedes-Benz", "Volvo"],
        "Intermediário": ["Toyota Corolla", "Honda Civic", "Jeep Compass"],
        "Econômico": ["Fiat Uno", "VW Gol", "Renault Kwid", "Chevrolet Onix"]
    }
    
    # Preço da diária por categoria (do mais caro ao mais barato)
    precos_diaria = {
        "Luxo": 1500.00,
        "Premium": 600.00,
        "Intermediário": 250.00,
        "Econômico": 100.00
    }
    
    # Busca a qual categoria o modelo pertence
    categoria_encontrada = None
    for cat, modelos in categorias.items():
        if modelo.lower() in [m.lower() for m in modelos]:
            categoria_encontrada = cat
            break
            
    if categoria_encontrada:
        valor_total = precos_diaria[categoria_encontrada] * dias
        print(f"Modelo: {modelo}")
        print(f"Categoria: {categoria_encontrada}")
        print(f"Valor Total por {dias} dias: R$ {valor_total:.2f}")
    else:
        print("Desculpe, esse modelo de carro não foi encontrado em nosso sistema.")

# Testando o código
carro = input("Digite o modelo do carro: ")
tempo = int(input("Quantos dias de aluguel? "))

calcular_aluguel(carro, tempo)
