from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from spacy.cli import download

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("Sayuki", tagger_language=ENGSM)

trainer = ListTrainer (chatbot)

trainer.train([
    'Ola!',
    'ola como vai?',
    'vou bem e voce?', 
    'tranquilo como esquilo e voce?', 
    'De boas na lagoa e voce?', 
    'Um dia quero viajar', 
    'Voce ja viajou muito?', 
    'Seria mesmo as estrelas um sol?', 
    'Eu sei apenas portugues', 
    'Voce conhece outros idiomas?', 
    'Gosta de animes?', 
    'Naruto é bom mas ja viu dororo?', 
    'Eu curto filmes de ação e aventura e voce?', 
    'Ja assistiu arquivo x?', 
    'eu gosto de ficar em casa lendo', 
    'Então me conte sobre voce', 
    'Ja ouviu a piada do piu?', 
    'E a diney cara? destruindo as bilheterias', 
    'Serio mesmo? to nem ai', 
    'Mentiram, tu jura mesmo?', 
    'E os babados da semana?', 
    'Então cinema hoje? o que ta em cartas?', 
    'Os filmes em cartas são muito ruims', 
    'Eu prefiro star wars do que jornada nas estrelas', 
    'Luke eu sou seu pai kof kof', 
    'Dave i cant let you do this', 
    'curioso ainda mais curioso', 
    'mas e paris ja foi?', 
    'Prefiro a inglaterra', 
    'Eu devia ser uma estrela la', 
    'Imagine so o ceu estrelado e nos dois juntos', 
    'Sim eu gosto', 
    'não eu não gosto', 
    'sim', 
    'Talvez', 
    'não sei', 
    '42', 
    'não', 
    'por que?', 
    'o que voce fez?', 
    'Seria possivel?', 
    'não pode ser'
    ])

os.system('cls')
while True:
    request = input('Voce:')
    response = chatbot.get_response(request)
    if request == 'parar':
        break
    print('Sayuki:', response)
