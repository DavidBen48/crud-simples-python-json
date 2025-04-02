# versão 1.5 -> separar os módulos que faz armazenar os dados para um arquivo próprio
import json
class ArmazenamentoDeDados:
  def __init__(self, arquivo = "estoque.json"):
    self.arquivo = arquivo
    self.carregar_dados()
  
  def carregar_dados(self):
    try:
      with open(self.arquivo, "r") as file:
          self.estoque = json.load(file)
    except FileNotFoundError:
      self.estoque = []

  def salvar_dados(self):
    with open(self.arquivo, "w") as file:
        json.dump(self.estoque, file, indent=4, ensure_ascii=False)
