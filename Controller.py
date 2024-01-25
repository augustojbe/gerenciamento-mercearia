from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria que deseja cadastrar já existe')
            
    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x)) 
        
        if len(cat) <= 0:
            print('A categoria que deseja remover não existe')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('Categoria removida com sucesso')  
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')
        

            
                    
    def alterarcategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()
        
        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))  
        
        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))   
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('A categoria alterada com sucesso')
                
                estoque = DaoEstoque.ler()
        
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, categoriaAlterada ), x.quantidade)
                          if(x.produto.categoria == categoriaAlterar) else(x), estoque))
        
                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                        arq.writelines('\n')
            else:
               print('A categoria que deseja alterar já existe') 
                
                   
        else:
            print('A categoria que deseja alterar não existe')
        
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
    
    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()
        if len(categorias) == 0:
            print('Categoria vazia')
        else:
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque:
    def cadastrarProdutos(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x)) 
        
        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto cadastrado com sucesso')
            else:
                print('Produto já existe no estoque')
        else:
            print('Categoria inesistente')
    
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('Produto removido com sucesso')
        else:
            print('O produto que deseja remover não existe')
        
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco 
                           + "|" + i.produto.categoria + "|" + str(i.quantidade) )
                arq.writelines('\n')
    
    def alterarProduto(self, nomeAlterar, novoNome, novoPreco, novaCategoria, novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreco, novaCategoria), novaQuantidade) 
                                 if(x.produto.nome == nomeAlterar) else(x), x))
                    print('Produto alterado com sucesso')
                else:
                    print('Produto já cadastrado')
            else:       
                print('O produto que deseja alterar não existe')
                
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco 
                            + "|" + i.produto.categoria + "|" + str(i.quantidade) )
                    arq.writelines('\n')
        else:
            print(" categoria informada não existe")
    
    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print('Estoque vazio')
        else:
            for i in estoque:
                print('==========Produtos==========')
                print(
                    f'Nome: {i.produto.nome}\n'
                    f'Preço: {i.produto.preco}\n'
                    f'Categoria: {i.produto.categoria}\n'
                    f'Quantidade: {i.quantidade}'
                    )
                print('============================')

class ControllerVenda:
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                    
                    vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                    
                    valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                    
                    DaoVenda.salvar(vendido)
                    
            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade))
        
        arq = open('estoque.txt', 'w')
        arq.write("")
        
        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines('\n')
        
        if existe == False:
            print('O produto não existe')
            return None
        elif not quantidade:
            print('A quantidade vendida não conte em estoque')
            return None
        else:
            print('Venda realizada com sucesso')
            return valorCompra
    
    def relatorioProdutos(self):
        vendas = DaoVenda.ler()
        produtos = []

        for i in vendas:
            nome = i.itensVendidios.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(filter(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                                       if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
        
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)
            
        print('Estes são o produto mas vendidos')
        a = 1
        for i in ordenado:
            print(f'==========produtos [{a}]==========')
            print(f'Produto: {i["produto"]}\n'
                    f'Quantidade: {i["quantidade"]}\n')
            a += 1
    
    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%y' )        
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%y' )  
        
        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data,'%d/%m/%y' ) >= dataInicio1 
                                         and datetime.strptime(x.data,'%d/%m/%y' ) <= dataTermino1, vendas))       
        
        cont = 1
        total = 0
        
        for i in vendasSelecionadas:
            print(f'=========Venda [{cont}=========]')
            print(f'Nome: {i.itensVendidios.nome}\n'
                  f'Categoria: {i.itensVendidios.categoria}\n'
                  f'Data: {i.data}\n'
                  f'Quantidade: {i.quantidadeVendida}\n'
                  f'Cliente: { i.comprador}\n'
                  f' Vendedor: { i.vendedor}\n')
            total += int(i.itensVendidios.preco) * int(i.quantidadeVendida)
            cont += 1
        print(f'Total vendido: {total}')

class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpf = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x)) 
        if len(listaCnpf) > 0:
            print('O cnpj já existe')
        elif len(listaTelefone) > 0:
            print('O o telefone já existe')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um cnpj ou telefone válido')
    
    
    def alterarfornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria):
        x = DaoFornecedor.ler()
        
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                est = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novoCategoria) if(x.nome == novoNome) else(x), x))
            else:
                print('Cnpj já existe')
        else:
            print('O fornecedor que deseja alterar não existe')
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('fornecedor alterado com sucesso')
            
    def removerfornecedor(self, nome):
        x = DaoFornecedor.ler()
        
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')
            return None
        
        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('fornecedor removido com sucesso')
    
    def mostrarfornecedores(self):
        forneceores = DaoFornecedor.ler()
        if len(forneceores) == 0:
            print('Lista de Fornecedores vazia')
        
        for i in forneceores:
            print('========Fornecedores========')
            print(
                f'Categoria fornecida: {i.categoria}'
                f'Nome: {i.nome}'
                f'Telefone: {i.telefone}'
                f'Cnpj: {i.cnpj}')
            
class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()
        
        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('Cpf já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente Cadastrado com sucesso')
            else:
                print('Digite um cpf ou telefone valido')
    
    def alterarCliente(self, nomeAlterar, novoNome, novoCpf, novoTelefone, novoEmail, novoendereco):
        x = DaoPessoa.ler()
        
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoCpf, novoTelefone, novoEmail, novoendereco) if (x.nome == nomeAlterar) else(x), x))
        else:
            print('O cliente que deseja alterar não existe')
        
        with open('cliente.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cpf + "|" + i.telefone + "|" + i.endereco)
                arq.writelines('\n')
            print('Cliente alterado com sucesso')
            
    def removerCliente(self, nome):
        x = DaoPessoa.ler()
        
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O Cliente que deseja remover não existe')
            return None
        
        with open('cliente.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('fornecedor removido com sucesso')
    
    def mostrarCliente(self):
        clientes = DaoPessoa.ler()
        for i in clientes:
            print('========Clientes========')
            print(
                f'Nome: {i.nome}'
                f'Telefone: {i.telefone}'
                f'Endereço: {i.endereco}'
                f'Email: {i.email}'
                f'Cpf: {i.cpf}')

class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()
        
        listaCpf = list(filter(lambda x: x.cpf, x))
        listaClt = list(filter(lambda x: x.clt, x))
        if len(listaCpf) > 0:
            print('CPF já existe')
        elif len(listaClt) > 0:
            print('Já existe um funcionario com essa clt')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario Cdastrado com sucesso')
            else:
                print('Digite um cpf ou telefone válido')
    
    def alterarfuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()
        
        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (x.nome == nomeAlterar) else(x), x))
        else:
            print('O funcionario que deseja alterar não existe')
        
        with open('funcionario.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.cpf + "|" + i.telefone + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Funcionario alterado com sucesso')
    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()
        
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print('O funcionario que deseja remover não existe')
            return None
    def mostrarFuncionario(self):
        funcionario = DaoFuncionario.ler()
        
        if len(funcionario) == 0:
            print('Lista de funcionarios vazia')
        
        for i in funcionario:
            print('=========Funcionario==========')
            print(f'Nome: {i.nome}'
                  f'Telefone: {i.telefone}'
                  f'Email: {i.email}'
                  f'Endereço: {i.endereco}'
                  f'CPF: {i.cpf}')
                


        
                    
                    
            
    
                

            

