import telebot

CHAVE_API = "5785602134:AAH91JtzSVs-u_keNGRFV_Q5TXdCjqg9utw"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

@bot.message_handler(commands=["finalizar"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """Pedido finalizado com Sucesso!
    
Para realizar, reclamar, verificar tempo de entrega ou cancelar um pedido clique aqui: /start""")    

@bot.message_handler(commands=["001"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Cerveja Skol Puro Malte 473ml adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["002"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Cerveja Brahma Duplo Malte 350ml adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["003"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Cerveja Itaipava 350ml adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["004"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Vodka Smirnoff 998ml adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["005"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Vodka Balalaika 1L adicionada ao Pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["006"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Vodka Ciroc Red Berry 750ml adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["007"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Água mineral 500ml sem gás adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["008"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Água mineral 500ml com gás adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["009"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Água mineral 1,5L sem gás adicionada ao pedido!

Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")


@bot.message_handler(commands=["010"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    Água mineral 1,5L com gás adicionada ao pedido!
    
Gostaria de adicionar mais algum item?

clique aqui para voltar aos produtos: /01
clique aqui para finalizar pedido /finalizar""")

@bot.message_handler(commands=["cerveja"])
def opcaocerveja(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    /001 Skol Puro Malte 473ml --- R$4,00 
/002 Brahma Duplo Malte 350ml --- R$3,59
/003 Itaipava 350ml --- R$2,65

clique aqui para voltar aos produtos: /01
clique aqui para voltar ao início: /iniciar""")

@bot.message_handler(commands=["vodka"])
def opcaovodka(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    /004 Smirnoff 998ml --- R$45,90 
/005 Balalaika 1L --- R$15,90
/006 Ciroc Red Berry 750ml --- R$158,29

clique aqui para voltar aos produtos: /01
clique aqui para voltar ao início: /iniciar""")

@bot.message_handler(commands=["agua"])
def opcaoagua(mensagem):
    bot.send_message(mensagem.chat.id , 
    """
    /007 Água mineral 500ml sem gás --- R$2,00 
/008 Água mineral 500ml com gás --- R$2,50
/009 Água mineral 1,5L sem gás --- R$5,00
/010 Água mineral 1,5L com gás --- R$5,00

clique aqui para voltar aos produtos: /01
clique aqui para voltar ao início: /iniciar""")


@bot.message_handler(commands=["01"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id ,
    """
    Selecione o que deseja abaixo!

    /cerveja para abrir lista de marcas e tamanhos de cervejas.
    /vodka para abrir lista de marcas e tamanhos de vodkas.
    /agua para selecionar a marca e o tamanho.

    clique aqui para voltar ao início: /iniciar""")


@bot.message_handler(commands=["02"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id ,
     "Para realizar uma reclamação, por favor envie um e-mail para APSCC8Q18@yahoo.com.br")


@bot.message_handler(commands=["03"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id , 
    """Segunda à Quinta: 20 minutos
Sexta à Domingo: 45 minutos   """)


@bot.message_handler(commands=["04"])
def opcao4(mensagem):
    bot.send_message(mensagem.chat.id , "Pedido cancelado com sucesso!")



@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Olá! tudo bem?
Nós somos a Drink Express! 
como podemos ajudar?
Escolha uma opção para continuar (Clique no item):
     /01 Realizar um pedido
     /02 Reclamar de um pedido
     /03 Verificar tempo médio de entrega
     /04 Cancelar pedido
Por gentileza, selecione uma das alternativas acima!"""
    bot.reply_to(mensagem, texto)


bot.polling()
