def minion_game(string):
    letras = 'BANANA'
    puntuacion_kevin = 0
    puntuacion_stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += (len(string)-i)
        else:
            stuart_score += (len(string)-i)
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")
    return string