import requests
import telebot
from googletrans import Translator

key_api = input("Sua chave API: ")

bot = telebot.TeleBot(key_api)

@bot.message_handler(commands=["frase"])
def frase_aleatoria(mensagem):
    url = "https://api.adviceslip.com/advice"
    trans = Translator()
    requisicao = requests.get(url)

    resposta = requisicao.json()
    frase = str(resposta["slip"]["advice"])
    traduzido = trans.translate(frase, dest="pt")

    bot.send_message(mensagem.chat.id, f"Essa foi a frase: {traduzido.text}")


@bot.message_handler(commands=["feargreed"])
def frase_aleatoria(mensagem):
    url = "https://api.alternative.me/fng/"
    requisicao = requests.get(url)
    
    resposta = requisicao.json()
    texto = f"""
Valor:  {resposta["data"][0]['value']}
Indicador: {resposta["data"][0]["value_classification"]}
    """
    
    bot.send_message(mensagem.chat.id, texto)


def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha um opção para continuar (clique no item):
    /frase uma frase aleatoria
    /feargreed mostra o fear e o greed do dia
    """
    bot.reply_to(mensagem, texto)

bot.polling()