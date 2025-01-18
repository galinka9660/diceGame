from game import Game

number_of_gamers = int(input("Wieviele Spieler sollen teilnehmen? " ))
all_players = list(range(1, number_of_gamers + 1))

while True:
    # first round
    results = []
    for i in range (len(all_players)):
        game = Game()
        result = game.roll_dice()
        results.append(result)

    # find a maximum result
    max_result = results[0]
    for res in results:   
        if res > max_result:
            max_result = res

    # making a list of gamers with maximum result
    winners = []
    for i in range(len(results)):
        if results[i] == max_result:
            winners.append(all_players[i])
        

    print(f"Spieler mit dem höchsten Ergebnis: {winners}")
    
    # checking winners
    if len(winners) == 1:  
        print(f"Gewinner ist Spieler {winners[0]}")
        break
    else:
        print(f"Unentschieden. Spieler {winners} spielen weiter.")
        all_players = winners



