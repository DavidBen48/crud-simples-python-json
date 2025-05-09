# 🏪 Controle de Estoques do Ben 📦

## 📜 Descrição

Este é um sistema simples de controle de estoque desenvolvido em Python, utilizando conceitos de Programação Orientada a Objetos (POO). O sistema permite adicionar, visualizar, atualizar e excluir produtos de um estoque armazenado em um arquivo JSON. 📂

## 📁 Estrutura do Projeto
 
```
/estoque
│-- main.py 🖥️
│-- GerenciamentoDeEstoque.py 🔄
│-- ArmazenamentoDeDados.py 💾
│-- estoque.json (gerado automaticamente) 📜
```

### 📌 Arquivos

- **main.py**: Responsável pela interface do usuário e interação com o sistema. 🖥️
- **GerenciamentoDeEstoque.py**: Contém a classe `GerenciamentoDeEstoque` com os métodos de manipulação do estoque. 🔄
- **ArmazenamentoDeDados.py**: Responsável pelo carregamento e salvamento de dados no arquivo JSON. 💾
- **estoque.json**: Arquivo onde os dados dos produtos são armazenados. 📜

## ⚙️ Funcionalidades

### 📜 Menu Principal

Ao iniciar o sistema, o usuário terá acesso ao seguinte menu:

```
== Controle de Estoques do Ben ==
=================================
+-------+---------------------------------+
| Opção | Descrição                       |
+-------+---------------------------------+
|   1   | Adicionar Produto               |
|   2   | Visualizar Produtos Existentes  |
|   3   | Atualizar Dados de Um Produto   |
|   4   | Deletar Um Produto              | 
|   0   | Sair do Sistema                 |
+----+------------------------------------+
```

### 🔹 Opções do Usuário

1. **➕ Adicionar Produto**

   - Solicita nome, quantidade e valor do produto. 🏷️
   - Gera um ID automático. 🔢
   - Salva no arquivo JSON. 💾

2. **📋 Visualizar Produtos Existentes**

   - Exibe uma tabela com ID, nome, quantidade e preço dos produtos. 📊
   - Informa caso não haja produtos cadastrados. ⚠️

3. **✏️ Atualizar Dados de Um Produto**

   - Permite alterar nome, quantidade ou preço de um produto. 🔄
   - Exige um ID válido para edição. 🔍

4. **❌ Deletar Um Produto**

   - Solicita confirmação antes de excluir um produto. ⚠️
   - Remove o produto do estoque e salva as alterações. 🗑️

5. **🚪 Sair do Sistema**

   - Salva automaticamente os produtos antes de sair. ✅

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o Python instalado (≥ 3.8). 🐍
2. Instale as dependências necessárias:
   ```bash
   pip install tabulate
   ```
3. Execute o arquivo `main.py`:
   ```bash
   python main.py
   ```

## 📌 Requisitos

- Python 3.8+ 🐍
- Biblioteca `tabulate` 🛠️

## 🚀 Melhorias Futuras

- Implementação de uma interface gráfica. 🖥️
- Melhor validação dos inputs dos usuários. ✅
- Adição de filtros para busca de produtos. 🔍

## ✨ Autor

David Ben ✍️ Copyright | 2025 | Declaro que o modelo do projeto foi 100% pensado por mim, sem me basear em algum outro projeto.

