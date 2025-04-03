from GerenciamentoDeEstoque import GerenciamentoDeEstoque
from tabulate import tabulate;

def main(sistema: GerenciamentoDeEstoque = GerenciamentoDeEstoque(), title: str = "== Controle de Estoques do Ben ==") -> any:   
 while True:      
    menu_de_opcoes = [
      ["1", "Adicionar Produto"],
      ["2", "Visualizar Produtos Existentes"],
      ["3", "Atualizar Dados de Um Produto"],
      ["4", "Deletar Um Produto"],
      ["0", "Sair do Sistema"]
    ];
    
    print(f"\n{title}")
    print("=" * len(title))
    print(tabulate(menu_de_opcoes, headers=["Opção", "Descrição"], tablefmt="grid"))
    
    opcao = input("Selecione uma opção: ")
    
    try:
      opcao = int(opcao)
    except ValueError:
      print("Por Favor, digite apenas números")
      continue;

    if opcao in [0, 1, 2, 3, 4]:
      match(opcao):
        case 0: 
          sistema.sair_do_sistema()
          break;
        case 1:
          sistema.adicionar_produto()
        case 2:
          sistema.visualizar_produtos()
        case 3:
          sistema.atualizar_produto()
        case 4:
          sistema.deletar_produto()
          
    else:
      print("Por Favor, escolha uma opção correta.")
        
if __name__ == "__main__":
  main();