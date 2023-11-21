import random

nomes = ['Aline', 'Arthur', 'Miguel', 'Bia', 'Guilherme']
emails = ['aline@gmail.com', 'rosa@gmail.com', 'arthur@gmail.com', 'david@gmail.com', 'panela@gmail.com']
telefones = [11944944, 11945544, 11993330, 11949303, 110404939]
cidades = ['São Paulo', 'Santos', 'Guaruja', 'Ilha Bela', 'Tokio']
estados = ['SP', 'RJ', 'RS', 'SC', 'PR']

print('Bem vindo ao gerador de dados de testes - Para finalizar o programa, digite "parar"')
print('---------------------')
print('Escolha uma ou mais opções abaixo para serem geradas aleatoriamente. Caso escolha uma segunda opção, por favor, separe com virgula.')

while True:
   usuario = (input('[1] - nome\n[2] - Email\n[3] - telefone\n[4] - Cidade \n[5] - Estado\n[6] - Fechar\n' ))
   usuario = usuario.split(',')
   
   resultados = []
   for usuarios in usuario:
       try:
           usuarios = int(usuarios)
           if usuarios == 1:
               resultados.append(random.choice(nomes))
           elif usuarios == 2:
               resultados.append(random.choice(emails))
           elif usuarios == 3:
               resultados.append(random.choice(telefones))
           elif usuarios == 4:
               resultados.append(random.choice(cidades))
           elif usuarios == 5:
               resultados.append(random.choice(estados))                  
           elif usuarios == 6:
               print('fechando app')
               exit()
           else:
               raise ValueError       
       
       except ValueError:
           print('Opção inválida, por favor escolha uma opção entre 1 e 6')
           

               
   for resultado in resultados:
       print(resultado)   
       
   repetir = input('Deseja repetir a operação? (s/n): ')
   if repetir.lower() != 's':
       break   
   
   salvar = input('Deseja salvar os resultados em um arquivo .txt? (s/n): ')
   if salvar.lower() == 's':
       with open('resultados.txt', 'w') as f:
           for resultado in resultados:
               f.write(resultado + '\n')
