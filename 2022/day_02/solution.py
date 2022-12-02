def get_move(action, opp_symbol):
    return ((action - 1) + opp_symbol) % 3

with open('input.txt', 'r') as file:
    
    strat = file.read()
    own_score = 0
    opp_score = 0

    for turn in strat.split('\n'):
        
        symbols = turn.split(' ')
        opp_symbol = ord(symbols[0]) - ord('A')
        action = ord(symbols[1]) - ord('X')
        own_symbol = get_move(action, opp_symbol)

        if opp_symbol == own_symbol:
            opp_score += 3
            own_score += 3
        else:
            if own_symbol == ((opp_symbol + 1) % 3):
                own_score += 6
            else:
                opp_score += 6

        opp_score += (opp_symbol + 1)
        own_score += (own_symbol + 1)

    print('final result: ', opp_score, ' : ', own_score)
