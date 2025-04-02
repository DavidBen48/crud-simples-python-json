import json
import random
import string
from tabulate import tabulate

class crud:
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

  def gerar_id(self) -> str:
      letras = ''.join(random.choices(string.ascii_uppercase, k=2))
      numeros = ''.join(random.choices(string.digits, k=4))   
      return letras + numeros 
  
  def adicionar_produto(self):
    nome_produto = input("Digite o nome do produto: ")
    quantidade_produto = int(input("Digite a quantidade do produto: "))
    valor_produto = float(input("Digite o valor do produto: "))
    
    produto_adicionado = {
      "id": self.gerar_id(),
      "nome": nome_produto,
      "quantidade": quantidade_produto,
      "valor": valor_produto
    }
    
    self.estoque.append(produto_adicionado)
    self.salvar_dados()
    
    print(f"Produto adicionado com sucesso! ID: {produto_adicionado['id']}")

  def visualizar_produtos(self):
    if not self.estoque:
      print("Nenhum produto na lista, ainda...")
      return;
    else:
      tabela = [
        [item["id"], item["nome"], item["quantidade"], f"R$ {item["valor"]:.2f}"]
        for item in self.estoque
      ]
      print(tabulate(tabela, headers=["ID", "Nome", "Quantidade", "Preço"], tablefmt="grid"))
  
  def atualizar_produto(self):
    id_informado = input("Digite o ID do produto que deseja atualizar: ").upper()
    produto = next((item for item in self.estoque if id_informado == item["id"]), None)
    
    if not produto:
      print("Produto não encontrado. Verifique se ele existe ou se o ID está correto.")
      return;
    else:
      print(f"Escolha o que quer atualizar no produto {produto["nome"]}:")
      print("[1] Nome\n[2] Quantidade\n[3] Preço")
      opcao_do_usuario = input("Selecione uma opção: ").strip()
      
      campos_de_opcao = {
        "1": "nome",
        "2": "quantidade",
        "3": "valor"
      }
      campo = campos_de_opcao.get(opcao_do_usuario)

      if not campos_de_opcao:
        print("Escolha apenas uma opção válida. Tente novamente.")
        return;
      
      novo_valor = input(f"Novo valor para {campo}: ")
      
      if campo == "quantidade":
        novo_valor = int(novo_valor)
      elif campo == "valor":
        novo_valor = float(novo_valor)
      else:
        novo_valor = str(novo_valor)
      
      produto[campo] = novo_valor
      self.salvar_dados()
      print("Produto atualizado com sucesso!")
      
  def deletar_produto(self):
    id_informado = input("ID do produto a ser excluído: ").upper()
    produto = next((item for item in self.database.estoque if item['id'] == id_informado), None)
    if not produto:
        print("Produto não encontrado.")
        return

    confirm = input(f"Tem certeza que deseja excluir o produto '{produto['nome']}'? [1] sim | [2] Não: ").lower()
    
    if confirm == "1":
      self.database.estoque.remove(produto)
      self.database.salvar_dados()
      print("Produto excluído com sucesso!")
    else: 
      print(f"Ação cancelada por:\n1- Desistência\n2- Escolheu errado")
      print(f"\nSe foi por escolher errado, tente novamente; Se não, desconsidere.")

  def sair_do_sistema(self):
    print("Você está saindo do sistema.")
    print("Carregando...")
    self.database.salvar_dados() # v1.5 -> salva, agora, de verdade, os dados antes de encerrar o programa.
    print("99%...")
    self.database.salvar_dados() # v1.5 -> confirmação de salvamento
    print("Prontinho! Todos os produtos foram salvos. Ao voltar, tudo ainda estará no estoque, se houver itens.")