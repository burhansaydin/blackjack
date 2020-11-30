import random
from art import logo
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')



def play():
    clear()
    want_play = input("Do you want to play BlackJack? Type 'y' or 'n'").lower()

    while want_play == "y":
        print(logo)
        your_cards = []
        com_cards = []
        your_current_score = 0
        com_current_score = 0
        deck = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        for a in range(2):
            your_cards.append(random.choice(deck))
            your_current_score += your_cards[a]
        com_cards.append(random.choice(deck))
        com_current_score += com_cards[0]

        print(f"Your cards {your_cards}, current score : {your_current_score}")
        print(f"Computer's first card : {com_cards}")

        if your_current_score == 21:
            com_cards.append(random.choice(deck))
            com_current_score += com_cards[-1]
            if com_current_score == 21:
                print("Draw..")
            else:
                print("BlackJack... You win")
        devam = input("Type 'y' to get another card, type 'n' to pass. :  ")

        while devam == "n":
            com_cards.append(random.choice(deck))
            com_current_score += com_cards[-1]
            if com_current_score < 18:
                devam = "n"
            elif com_current_score > 21 and 11 not in com_cards:
                print(
                    f"You win. :) Your score is {your_current_score}, dealer is {com_current_score}"
                )
                want_play = "n"
                break

            elif your_current_score > com_current_score:
                print(
                    f"You win. :) Your score is {your_current_score}, dealer is {com_current_score}"
                )
                want_play = "n"
                break
            elif your_current_score == com_current_score:
                print("Draw..")

                want_play = "n"
                break
            else:
                print(
                    f"You lose. :( Your score is {your_current_score}, dealer is {com_current_score}"
                )
                want_play = "n"
                break

        while devam == "y":
            your_cards.append(random.choice(deck))
            your_current_score += your_cards[-1]
            print(f"Your cards: {your_cards}' current score: {your_current_score}")
            print(f"Computer's first card : {com_cards}")
            if your_current_score > 21 and 11 not in your_cards:
                com_cards.append(random.choice(deck))
                com_current_score += com_cards[-1]
                print(f"You lose..Your score is {your_current_score}, dealer is {com_current_score} ")
                play()
            elif your_current_score > 21 and 11 in your_cards:
                x = your_cards.index(11)
                your_cards[x] = 1

            devam = input("Type 'y' to get another card, type 'n' to pass. :  ")
            while devam == "n":
                com_cards.append(random.choice(deck))
                com_current_score += com_cards[-1]
                if com_current_score < 18:
                    devam = "n"
                elif com_current_score > 21 and 11 not in com_cards:
                    print(
                        f"You win. :) Your score is {your_current_score}, dealer is {com_current_score}"
                    )
                    want_play = "n"
                    break
                elif your_current_score > com_current_score:
                    print(
                        f"You win. :) Your score is {your_current_score}, dealer is {com_current_score}"
                    )
                    want_play = "n"
                    break
                elif your_current_score == com_current_score:
                    print("Draw..")
                    want_play = "n"
                    break
                else:
                    print(
                        f"You lose. :( Your score is {your_current_score}, dealer is {com_current_score}"
                    )
                    break


play()