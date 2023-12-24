pokedex = []
contador = 0

def adicionar_pokemon():
    global contador
    while True:
     nome = input("Nome do Pokemon: ")
     
     # Condição para que se o nome do Pokemon ja tiver na Pokedex, não permitir adiciona-lo.
     for pokemon in pokedex:
        if pokemon["nome"] == nome:
            print("Este nome de Pokémon já existe na Pokédex. Tente novamente.")
            break
     else:        
      tipo = input("Tipo do Pokemon: ")
      level = int(input("Nível do Pokemon: "))
      id_pokemon = len(pokedex) + 1
      pokemon = {"id": id_pokemon, "nome": nome, "tipo": tipo, "level": level}
      pokedex.append(pokemon)
      contador +=1
    
      print(f"{nome}, com ID {id_pokemon} foi adicionado à Pokedex.")
      print(f"Total de Pokémons na pokedex: {contador}")
      break

def listar_pokemon():
    if pokedex:
        print("Pokémon na Pokedex:")
        for pokemon in pokedex:
            print(f"id: {pokemon['id']}, Nome: {pokemon['nome']}, Tipo: {pokemon['tipo']}, level: {pokemon['level']}")
    else:
        print("A Pokedex está vazia.")
    print(f"Total de Pokémons na pokedex: {contador}")

def procurar_pokemon():
    nome_procurado = input("Digite o nome ou tipo do Pokémon que deseja procurar: ")
    for pokemon in pokedex:
        # Permitir procurar por tipo ou nome.
        if pokemon['nome'] == nome_procurado or pokemon['tipo'] == nome_procurado:
            print(f"id: {pokemon['id']}, Nome: {pokemon['nome']}, Tipo: {pokemon['tipo']}, level: {pokemon['level']}")
        else:
            print(f"{nome_procurado} não encontrado na Pokedex.")
        print(procurar_pokemon)

def atualizar_pokemon():
    nome_atualizar = input("Digite o nome do Pokémon que deseja atualizar: ")
    for pokemon in pokedex:
         if pokemon['nome'] == nome_atualizar:
              print(f'Atualize as informações de {nome_atualizar}:')
              nome = input("Novo nome do Pokémon: ")
              tipo = input("Novo tipo do Pokémon: ")
              level = input("Novo level do Pokémon: ")
              pokemon['nome'] = nome
              pokemon['tipo'] = tipo
              pokemon['level'] = level
              print(f'Informações de {nome_atualizar} foram atualizadas com sucesso!')
              break
    else:
     print(f"{nome_atualizar} não encontrado na Pokedex.")

def excluir_pokemon():
     nome_excluir = input("Digite o nome do Pokémon na qual você quer excluir: ")
     for pokemon in pokedex:
          if pokemon['nome'] == nome_excluir:
               pokedex.remove(pokemon)
               print(f'{nome_excluir} foi excluído da Pokedex!')
          else:
               print(f"{nome_excluir} não encontrado na Pokedex.")

def menu():
  print("\nO que você deseja fazer?")
  print("1. Adicionar Pokémon")
  print("2. Listar Pokémon")
  print("3. Procurar Pokémon")
  print("4. Atualizar dados do Pokémon")
  print("5. Excluir Pokémon")
  print("6. Sair")
  print("7. Salvar")
    
# Execução das Funções 

while True:
    menu()
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
            adicionar_pokemon()
    elif escolha == '2':
            listar_pokemon()
    elif escolha == '3':
            procurar_pokemon()
    elif escolha == '4':
         atualizar_pokemon()
    elif escolha == '5':
         excluir_pokemon()
    elif escolha == '6':
        print("Obrigado por usar a Pokedex!")
        break
    elif escolha =='7':
         file = open("pokedex.txt", "w")
         file.write(str(pokedex))
         file.close()
         print("Salvo com sucesso.")
    else:
        print("Escolha uma opção válida.")
