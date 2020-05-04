def sports_team(kind, *scorers, **players):
    print("-"*40)
    print("{0} team lineup\n".format(kind))
    for player in players.keys():
        print(player, ":", players[player])
    print("-"*40)
    print("Last couple minutes of the game:\n")
    for scorer in scorers:
        print("{0} SCORED!!!".format(scorer))
    print("-"*40)


def main():
    sports_team("Football", "Neymar", "Neymar", "Firmino", 
    Goalkeeper='Alisson', Rightback='Daniel Alves', 
    Centerback1='Felipe', Centerback2='Marquinhos',
    Leftback='Alex Telles', Defensive_Midfielder1='Casemiro', 
    Defensive_Midfielder2='Fabinho', Attacking_Midfielder='Neymar', 
    Left_Winger='Cebolinha', Right_Winger='Jesus', 
    Center_Forward='Firmino')


main()