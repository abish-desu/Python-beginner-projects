from os import system
from minichat import minichat

chatbot = minichat.Minichat(name="Abish")

system("cls")
while True:
    question = input("You: ")
    answer = chatbot.chat(question)
    print("Bot:", answer)