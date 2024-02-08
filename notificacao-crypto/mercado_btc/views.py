from django.shortcuts import render
import requests
from django.http import HttpResponse
from mercado_bitcoin import DataAPI

from django.utils import timezone
import datetime
import json


def retornaListaString(ticker, crypto):
    minimo = ticker['high']
    maximo = ticker['low']
    volume = ticker['vol']
    compra = ticker['buy']
    venda = ticker['sell']
    preco_abertura = ticker['open']
    ultimo_preco = ticker['last']
    data = ticker['date']

    mensagem = f"Valores {crypto}:\nminimo: {minimo}\nMaximo: {maximo}\nVolume: {volume}\nUltimo_preco: {ultimo_preco}\nCompra: {compra}\nVenda: {venda}\nPreço de abertura: {preco_abertura}\nData: {data}"

    return mensagem


def buscaCotacaoMercadoBtc(request):
    crypto = ''
    lista = ''
    listaCrypto = ['BTC', 'ETH', 'LTC']
    dicionarioCotacao = {}

    for crypto in listaCrypto:
        dicionarioCotacao[''+crypto+'']={}
        resp = DataAPI.ticker(crypto)
        dadosCrypto = json.loads(resp.text)

        if len(lista) > 0:
            lista += '\n\n'+retornaListaString(dadosCrypto['ticker'], crypto)
        else:
            lista = retornaListaString(dadosCrypto['ticker'], crypto)

        for key, chave in dadosCrypto['ticker'].items():
            dicionarioCotacao[''+crypto+''][''+key+'']=chave

    return lista


def funcaoEnviaMensagem(request):
    conteudoMensagem = buscaCotacaoMercadoBtc(request)
    url = "https://api.callmebot.com/whatsapp.php"

    params = {
        'phone': '+5518996768677',
        'text': conteudoMensagem,
        'apikey': '8067377'
    }

    # response = requests.get(url, params=params)

    # if response.status_code == 200:
    #     # Requisição bem-sucedida
    #     return HttpResponse('Requisição enviada com sucesso')
    # else:
    #     # Tratar outros códigos de status, se necessário
    #     return HttpResponse('Falha ao enviar a requisição')
    return HttpResponse('requisicao enviada')