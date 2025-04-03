#############################################################################################################################################################
# Autor:      Gabriela Terixeira
# Email:      gabyteixeiragt2@gmail.com
# Criado:     27/08/2022
# Projeto:    Análise de Pareto - Hora do código
#
# Descrição:  Elabore um código na linguagem de sua preferência que receba como entrada os 
#             dados (variável nominal) de um arquivo TXT ou CSV e apresente como saída uma tabela 
#             organizada na forma propícia para Análise de Pareto.
#
# Professor:  Luiz Carlos Dos Santos Filho
#############################################################################################################################################################

def max_in_list(l):
    max_value = ''
    maior=0

    for _ in l:
        if isinstance(_, list):
            max_value = max_in_list(_)
            maior=len(max_value)

        if len(_) > len(max_value):
            max_value = _
            maior=len(max_value)

    return(maior)
nome_tabela = input("Qual o nome da tabela? ")

#___Armazenando dados.txt em uma lista doc__________
with open ("dados.txt", "r") as arquivo:
  doc= arquivo.read().split("\n")
#___________________________________________________

tamanho_espc=max_in_list(doc)

#____Armazendando dados da frequencia indicativa____

f_indic= {} #Dicionário onde serão contabilizadas as frequências indicativa
fi_ordenada = {} #Dicionário onde serão contabilizadas as frequências indicativa em ordem decrescente (do maior para o menor)

for item in doc: #Para cada item na lista doc
    if(item not in f_indic): #Se o item não está em "frequências indicativa"
        f_indic[item]= doc.count(item) #Adicione o item como chave, conte quantas vezes esse item aparece em "doc" e adicione como valor
        
for item in sorted(f_indic, key=f_indic.get, reverse=True):
    #Depois, ordene todos os ítens em f_indic em ordem decrescente
    fi_ordenada[item]=f_indic[item]
    #e adicione cada item no dicionário de frequências indicativa em ordem decrescente
    
#___________________________________________________

    
    
#____Armazendando dados da frequencia percentual____

f_percent= {} #Dicionário onde serão contabilizadas as frequências percentual
fp_ordenada={} #Dicionário onde serão contabilizadas as frequências percentual de forma decrescente

for item in doc: #Para cada item na lista doc
    if(item not in f_percent): #Se o item não está no dicinário "frequência percentual"
        f_percent[item]= (doc.count(item)/len(doc))
        # Conte quantas vezes aquele item aparece na lista doc, divida pelo total de itens dela
for item in sorted(f_percent, key=f_percent.get, reverse=True):
    #Depois, ordene todos os ítens em f_percent em ordem decrescente
    fp_ordenada[item]=f_percent[item]
    #e adicione cada item no dicionário fp_ordenada
    
#___________________________________________________


#____Armazendando dados da frequencia Acumulada_____

fp_ord_chaves=list(fp_ordenada.keys())#Armazena as chaves do dicionário fp_ordenada
fp_ord_lista=list(fp_ordenada.values()) #Armazena os ítems da fp_ordenada em uma nova lista chamada fp_ord_lista
soma = 0 #Criando uma variável soma, onde será armazenado momentaniamente o resultado de cada soma do "for"
comprimento = len(fp_ord_lista) #Armazena a quantidade de itens contidos na lista fp_ord_lista
f_acum = [] #Nova lista onde será armazenado a frequencia acumulada
for i in range(comprimento): #Para cada item dentro da quantidade de itens da fp_ord_lista:
        soma = soma + fp_ord_lista[i] #Some o valor atual da variável "soma" com o valor do ítem analizado, armazene esse novo valor na variável "soma"
        f_acum.append(soma)#e adicione ele na lista "f_acum"
f_acum_dict = dict(zip(fp_ord_chaves,f_acum)) #A função zip() retorna uma lista de tuplas e a função dict() transforma tuplas em dicionário
#Cria um novo dicionário herdando as chaves do fp_ordenada e a somatória dos valores do f_acum

#___________________________________________________


#____Armazendando nomes dos erros___________________

lista_erros= list(fi_ordenada.keys())
#armazene todas as chaves (nomes dos erros) na lista_erros

#___________________________________________________
print(lista_erros)
print(fi_ordenada)
print(fp_ordenada)
print(f_acum_dict)

#____Printando tabela_______________________________
print("\n")
print ("_"*62)
print("  ")
print (nome_tabela.center(62))
print ("_"*62)
print('{:<2} {:<6} {:<2} {:<4} {:<2} {:<4} {:<4} {:<4}'.format("|", "Erros", "|", "N de Ocorrencias", "|","F.percentual", "|", "F.Acum"))
for item in lista_erros:
    print('{:<4} {:<4} {:<8} {:<10} {:<4} {:<10.2%} {:<4} {:<4.2%}'.format("|", item, "|", fi_ordenada[item], "|",fp_ordenada[item], "|", f_acum_dict[item]))
print ("_"*62)
print('{:<2} {:<6} {:<8} {:<10} {:<4} {:<10.2%} {:<4} {:<4}'.format("|", "Total", "|", len(doc), "|", sum(fp_ordenada.values()), "|", " "))
   