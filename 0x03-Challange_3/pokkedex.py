def juegoPekkemon(LetrasCarlos:str, LetrasValeria:str, Pekkemons:str):
    carlos = list(LetrasCarlos)
    valeria = list(LetrasValeria)
    pekkemones = list(Pekkemons)
    dex = []
    score_carlos = score_valeria = 0
    for i in pekkemones:
        if i in carlos and i in valeria:
            score_carlos += 1
            score_valeria += 1
        if i in valeria and not i in carlos:
            score_valeria += 1
        if i in carlos and not i in valeria:
            score_carlos += 1
        if score_carlos == score_valeria:
            dex.append('P')
        elif score_carlos > score_valeria:
            dex.append('C')
        else:
            dex.append('V')
    return(dex)