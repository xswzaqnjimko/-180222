# -*- coding: utf-8 -*-

def multiple_choice_loop():
    answer_i = input("私の贈り物が好きですか"
                     "\n 1 - Yes / 2 - No / 3 - No Idea "
                     "\n My dear, you know I can't write sugoi programs yet"
                     "\n  - simply enter the number, ねぇぇ~ : ")
    try:
        answer = float(answer_i)
    except ValueError:
        print("\n "
              "Come on, darling, answer the question(ಡ ಡ) \n")
    else:
        if answer == 1:
            print("\n "
                  "Haha! \n"
                  "~【dianjihuidao ≈1:(φ-1)】(hhhh \n")
        elif answer == 2:
            print("\n"
                  "Come and tell me why, please ♡ \n")
        elif answer == 3:
            print("\n"
                  "Interesting answer, I like it~ \n"
                  "| Would you open the birthday card for me? | \n")
        else:
            print("\n "
                  "Come on, darling(ಡ^ಡ) \n")
    play_again()


def play_again():
    again_ka_i = input("Wanna change your answer? 1 - Yes / 2 - No : ")
    try:
        again_ka = float(again_ka_i)
    except ValueError:
        print("\n "
              "cielo~逸れるな=w= \n")
        play_again()
    else:
        if again_ka == 1:
            print("\n")
            multiple_choice_loop()
        elif again_ka == 2:
            print("\n")
            are_you_sure()
        else:
            print("\n cariño~わざとしたよね=w= \n")
            play_again()

#あなた、やっぱり此処に来たねwww
#   told you~ just go back to the card =v=#
# > teach me when we meet♡♡!!

def are_you_sure():
    sure_ka_i = input("Are you sure? \n"
                      "1 - Yes / 2 - No / 3 - No Idea : ")
    try:
        sure_ka = float(sure_ka_i)
    except ValueError:
        print("\n "
              "わざとだな、Horaceさん~! \n")
        are_you_sure()
    else:
        if sure_ka == 1:
            print("\n"
                  "Wow I didn't(x) expect this ~ See you → →+ \n")
            quit_ka = input("Enter 'q' to quit: ").lower()
            if quit_ka == "q":
                quit()
            else:
                print("\n 轩儿呀~~╮(╯╰)╭ \n"
                      "~I'll just go back: \n")
                are_you_sure()
        elif sure_ka == 2:
            print("\n"
                  "Jya one more chance~ \n")
            play_again()
        elif sure_ka == 3:
            print("\n"
                  "流石选恐(x)www (かわいい~ \n")
            play_again()
        else:
            print("\n"
                  "ほら、なにをしたよあなたԾ Ծ \n"
                  "自分で解決しろԾ Ծ")


def run_multiple_choice():
    multiple_choice_loop()


run_multiple_choice()

