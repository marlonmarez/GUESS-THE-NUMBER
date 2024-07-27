import random

print("GAME ADIVINHE O NUMERO")
show_number = input("ESCOLHA O N° TETO:")

if show_number.isdigit():
    show_number = int(show_number)
else:
    print("ERRO! FAVOR DIGITAR UM NUMERO.")
    quit()

random_number = random.randint(1, show_number)

while True:
    user_number = input("Digite seu Numero: ")

    if user_number.isdigit():
        user_number = int(user_number)
    else:
        print("ERRO! FAVOR DIGITAR UM NUMERO.")
        continue
    

    if user_number == random_number:
        print("VOCÊ ACERTOU!")
        break
    elif user_number > random_number:
        print("VOCÊ CHUTOU ALTO! O NUMERO É MENOR QUE ISSO...")
    else:
         print("VOCÊ CHUTOU BAIXO! O NUMERO É MENOR QUE ISSO...")