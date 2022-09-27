import telebot

CHAVE_API = "5785602134:AAH91JtzSVs-u_keNGRFV_Q5TXdCjqg9utw"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True
@bot.message_handler(commands=["cerveja"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Skol Puro Malte 473ml --- R$4,00 
Brahma Duplo Malte 350ml --- R$3,59
Itaipava 350ml --- R$2,65
clique aqui para voltar ao início: /iniciar""")

@bot.message_handler(commands=["vodka"])
def opcaovodka(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Smirnoff 998ml --- R$45,90 
Balalaika 1L --- R$15,90
Ciroc Red Berry 750ml --- R$158,29
clique aqui para voltar ao início: /iniciar""")

@bot.message_handler(commands=["agua"])
def opcaoagua(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Água mineral 500ml sem gás --- R$2,00 
Água mineral 500ml com gás --- R$2,50
Água mineral 1,5L sem gás --- R$5,00
Água mineral 1,5L com gás --- R$5,00
clique aqui para voltar ao início: /iniciar""")



@bot.message_handler(commands=["1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id ,
    """
    Selecione o que deseja abaixo!
    /cerveja para abrir lista de marcas e tamanhos de cervejas.
    /vodka para abrir lista de marcas e tamanhos de vodkas.
    /agua para selecionar o tipo e tamanho.""")

@bot.message_handler(commands=["2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id ,
     "Para realizar uma reclamação, por favor envie um e-mail para APSCC8Q18@yahoo.com.br")

@bot.message_handler(commands=["3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id , 
    """Segunda à Quinta: 20 minutos
Sexta à Domingo: 45 minutos   """)

@bot.message_handler(commands=["4"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id , "Pedido cancelado com sucesso!")


 


@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no item):
     /1 Realizar um pedido
     /2 Reclamar de um pedido
     /3 Verificar tempo médio de preparo/entrega
     /4 Cancelar pedido
Por gentileza, selecione uma das alternativas acima!"""
    bot.reply_to(mensagem, texto)


bot.polling()
