import Controller
import os.path

def criarArquivos(*nome):
    for i in nome:
        if not os.path.exists(i):
            with open(i, 'w') as arq:
                arq.write("")
                
criarArquivos("categoria.txt", "clientes.txt", "estoque.txt", "fornecedores.txt", "funcionarios.txt", "venda.txt" )

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar (Categoria)\n"
                          "Digite 2 para acessar (Estoque)\n"
                          "Digite 3 para acessar (Fornecedor)\n"
                          "Digite 4 para acessar (Cliente)\n"
                          "Digite 5 para acessar (Funcionario)\n"
                          "Digite 6 para acessar (Vendas)\n"
                          "Digite 7 para ver os produtos mas vendidos\n"
                          "Digite 8 para sair\n"))
        
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                decidir = int(input("Digite 1 para cadastrar categoria\n"
                                    "Digite 2 para remover uma categoria\n"
                                    "Digite 3 para alterar uma categorias\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))
                
                if decidir == 1:
                    categoria = input('Digite a categoria que deseja cadastrar\n')
                    cat.cadastraCategoria(categoria)
                elif decidir == 2:
                    categoria = input('Digite a categoria que deseja remover\n')
                    cat.removerCategoria(categoria)
                elif decidir == 3:
                    categoria = input('Digite a categoria que deseja alterar\n')
                    novaCategoria = input('Digite a nova categoria\n')
                    cat.alterarcategoria(categoria, novaCategoria)
                elif decidir == 4:
                    cat.mostrarCategoria()
                else:
                    break
        
        elif local == 2:
            cat = Controller.ControllerEstoque()
            while True:
                decidir = int(input("Digite 1 para cadastrar um produto\n"
                                    "Digite 2 para remover um produto\n"
                                    "Digite 3 para alterar um produto\n"
                                    "Digite 4 para mostrar as categorias cadastradas\n"
                                    "Digite 5 para sair\n"))
                
                if decidir == 1:
                    produto = input('Digite o produto que deseja cadastar\n')
                    cat.cadastrarProdutos(produto)
                elif decidir == 2:
                    produto = input('Digite o produto que deseja remover\n')
                    cat.removerProduto(produto)
                elif decidir == 3:
                    produto = input('Digite o produto que deseja alterar\n')
                    novoProduto = input('Digite o novo produto')
                    cat.alterarProduto(produto, novoProduto)
                elif decidir == 4:
                   cat.mostrarEstoque()
                else:
                    break
        
        elif local == 3:
            cat = Controller.ControllerFornecedor()
            while True:
                decidir = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar um fornecedor\n"
                                    "Digite 5 para sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do Fornecedor: \n")
                    cnpj = input("Digite o CNPJ do fornecedor: \n")
                    telefone = input("Digite o telefone do fornecedor: \n")
                    categoria = input('Digite a categoria do fornecedor: \n')
                    cat.cadastrarFornecedor(nome, cnpj, telefone, categoria)
                elif decidir == 2:
                    nome = input("Digite o nome do Fornecedor: \n")
                    cat.removerfornecedor(nome)
                elif decidir == 3:
                    nomeAlterar= input("Digite o nome do fornecedor que deseja alterar: \n")
                    novoNome= input("Digite o novo nome do Fornecedor: \n")
                    novoCnpj= input("Digite o CNPJ do fornecedor: \n")
                    novoTelefone= input("Digite o novo telefone do Fornecedor: \n")
                    novaCategoria= input("Digite a nova categoria do Fornecedor: \n")
                    
                    cat.alterarfornecedor(nomeAlterar, novoNome, novoCnpj, novoTelefone, novaCategoria)
                elif decidir == 4:
                    cat.mostrarfornecedores()
                else:
                    break
                
        elif local == 4:
            cat = Controller.ControllerCliente()
            while True:
                decidir = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar um clientes\n"
                                    "Digite 5 para sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do Cliente: \n")
                    cpf = input("Digite o CPF do cliente: \n")
                    telefone = input("Digite o telefone do cliente: \n")
                    email = input('Digite o email do cliente: \n')
                    endereco = input('Digite o endereço do cliente: \n')
                    
                    cat.cadastrarCliente(nome, cpf, telefone, email, endereco)
                    
                elif decidir == 2:
                    cliente = input("Digite o nome do cliente quedeseja remover: \n")
                    cat.removerCliente(cliente)
                
                elif decidir == 3:
                    nomeAlterar= input("Digite o nome do Cliente que deseja alterar: \n")
                    novoNome= input("Digite o novo nome do Cliente: \n")
                    novoTelefone= input("Digite o novo telefone do cliente: \n")
                    novoCpf= input("Digite o novo CPF do cliente: \n")
                    novoEmail= input("Digite o nova Email do Cliente: \n")
                    novaEndereco= input("Digite o nova endereço do Cliente: \n")
                    cat.alterarCliente(nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novaEndereco)
                elif decidir == 4:
                    cat.mostrarCliente()
                else:
                    break
        elif local == 5:
            cat = Controller.ControllerFuncionario()
            while True:
                decidir = int(input("Digite 1 para cadastrar um funcionario\n"
                                    "Digite 2 para remover um funcionario\n"
                                    "Digite 3 para alterar um funcionario\n"
                                    "Digite 4 para mostrar funcionarios\n"
                                    "Digite 5 para sair\n"))
                if decidir == 1:
                    clt = input('Digite o numero da clt do funcionario\n ')
                    nome = input('Digite o nome do funcionario\n ')
                    telefone = input('Digite o telefone do funcionario\n ')
                    cpf = input('Digite o numero do cpf do funcionario\n')
                    emal= input('Digite o email do funcionario \n')
                    endereco= input('Digite o endereço do funcionario\n ')
                    cat.cadastrarFuncionario(clt, nome, telefone, cpf, emal, endereco)
                elif decidir == 2:
                    funcionario = input("Digite o nome do funcionario quedeseja remover: \n")
                    cat.removerCliente(funcionario)
                elif decidir == 3:
                    nomeAlterar= input("Digite o nome do Funcionario que deseja alterar: \n")
                    novoClt= input("Digite a nova CLT do funcionario: \n")
                    novoNome= input("Digite o novo nome do funcionario: \n")
                    novoTelefone= input("Digite o novo telefone do funcionario: \n") 
                    novoCpf= input("Digite o novo CPF do funcionario: \n")
                    novoEmail= input("Digite o novo Email do funcionario: \n")
                    novoEndereco= input("Digite o novo Endereço do funcionario: \n")
                    cat.alterarfuncionario(nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco)
                elif decidir == 4:
                    cat.mostrarFuncionario()
        elif local == 6:
            cat = Controller.ControllerVenda()
            while True:
                decidir = int(input("Digite 1 para realizar uma venda \n"
                                    "Digite 2 para ver as vendas \n"
                                    "Digite 3 para sair\n"))
                
                if decidir == 1:
                    nome = input("Digite o nome do produto: \n")
                    vendedor = input("Digite nome do vendedor: \n")
                    comprador = input("Digite o nome do comprador? \n")
                    quantidaeVendida = input("Digite a quantidade vendida: \n")
                    cat.cadastrarVenda(nome, vendedor, comprador, quantidaeVendida)
                elif decidir == 2:
                    dataInicio = input('Digite a data de Inicio no formato dia/mes/ano: \n')
                    dataTermino = input('Digite a data de Termino no formato dia/mes/ano: \n')
                    cat.mostrarVenda(dataInicio, dataTermino)
                else:
                    break
        elif local == 7:
            a = Controller.ControllerVenda()
            a.relatorioProdutos()
        else:
            break
                    
                    
                    
                    
                    
                    
                    
                                 
                    
                    