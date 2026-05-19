# a palavra "class" e usada para criar uma classe.
# uma classe funciona como um molde para criar objetos.
class carro:
  pass
# "def" definir uma funcao ou metodo.
# __init__" e o metodo construtor da classe.
# ele e um executado automaticamente quando um objeto e criado 

# "self" representa o proprio objeto.
# E atraves do self que acessamos atributos e metodos  do abjeto 

# "marca","modelo","ano", e "velocidade"
# sao parametros recebidos pela classe.

def __init__(self,marca, modelo ,ano , velocidadade=0):
  
  self.marca = marca
  self.modelo = modelo
  self.ano = ano
  self.velocidade = velocidadade


  carro1 = carro("chevrolet","S10", 2013)
  
  # Exibir informacoes do carro
  print(F"marca: {carro1.marca}")
  print(F"modelo: {carro1.modelo}")
  print(F"ano: {carro1.ano}")
  
