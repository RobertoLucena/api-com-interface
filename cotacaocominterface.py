import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    requisicao_dic = requisicao.json()

    valor_dolar = requisicao_dic["USDBRL"]["bid"]
    valor_euro = requisicao_dic["EURBRL"]["bid"]
    valor_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f'''
    Dólar: R$ {valor_dolar} reais
    Euro: R$ {valor_euro} reais
    BTC: R$ {valor_btc} reais
    '''
    #print(texto)

#editando parâmetro TEXT dentro da variável texto_cotações assim que o botão for clicado e a função rodar
    texto_cotacoes["text"] = texto

#pegar_cotacoes()

#toda interface com TKinter inicia com janela = Tk() e termina com janela.mainloop()
#não é necessário escrever Tkinter.tk pois importamos assim: from tkinter import *
janela = Tk()

#alterando o nome da janela
janela.title("Cotação atual das Moedas")

#colocando texto dentro da janela
texto_orientação = Label(janela, text='Clique no Botão para ver as cotações das moedas')

#posicionando o texto
texto_orientação.grid(column=0, row=0, padx=10, pady=10)

#criando botão, cuidado com a função, vai sem o parênteses
botao = Button(janela, text='BUSCAR COTAÇÃO', command=pegar_cotacoes)

#posicionando botão
botao.grid(column=0, row=1, padx=10, pady=10)

#criando texto onde as cotações ficarão e posicionando
texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()