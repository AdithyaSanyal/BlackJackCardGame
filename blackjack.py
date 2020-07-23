from random import shuffle
def DECK():
    deck=[]
    for suits in ["DIAMOND ","SPADE ","HEART ","CLUB "]:
        for numbers in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            deck.append(suits+numbers)
    shuffle(deck)
    return deck

def POINTCOUNTER(Cards):
    Count=0
    AceCount=0
    for card in Cards:
        if(card[-1]=='0' or card[-1]=='J' or card[-1]=='Q' or card[-1]=='K'):
            Count+=10
        elif(card[-1]=='A'):
            AceCount+=1
        else:
            Count+=int(card[-1])
    if(AceCount==1 and Count<=10):
        Count+=11
    else:
        Count+=AceCount
    return Count

def STARTINGCARDS(Deck):
    DealerCard=[]
    PlayerCard=[]
    DealerCard.append(Deck.pop())
    DealerCard.append(Deck.pop())
    PlayerCard.append(Deck.pop())
    PlayerCard.append(Deck.pop())
    
    while(POINTCOUNTER(DealerCard)<=16):
        DealerCard.append(Deck.pop())
    
    return [DealerCard,PlayerCard]
money=0    
while True:
    try:
        money=float(input("ENTER THE AMOUNT YOU WANT TO INVEST (in Rupees):"))
    except:
        print("PLEASE ENTER AN AMOUNT")
        continue
    else:
        break
renew=''
while(renew!="NO"):
    if(money==0):
        print("WE ARE SORRY TO INFORM YOU THAT YOU HAVE GONE BANRUPT,")
        print("YOU CAN'T PLAY THIS GAME ANYMORE")
        break
    while True:
        try:
            print("ENTER THE AMOUNT OF MONEY YOU WANT TO BET ON THIS TURN?")
            amt=float(input())
        except:
            print("PLEASE ENTER AN AMOUNT\n")
            continue
        else:
            break
    if(money>=amt):
        money-=amt
        print("AMOUNT ACCEPTED! YOU CAN PLAY")
        print(f"BALANCE IN YOUR ACCOUNT= {money} Rs\n")
    else:
        print("YOU DON'T HAVE ENOUGH MONEY FOR SUCH A BET")
        continue
    
    game=""
    CardDeck=DECK()
    PlayingCards=STARTINGCARDS(CardDeck)
    DealersCards=PlayingCards[0]
    PlayersCards=PlayingCards[1]
    
    
    while (game!='EXIT'):
        DealersScore=POINTCOUNTER(DealersCards)
        PlayersScore=POINTCOUNTER(PlayersCards)
                                    
        print("Dealers Cards:")
        print(f"[{DealersCards[0]}]")
        print("\n")
        print("Players Cards:")
        print(PlayersCards)
        print("\n")
        if(PlayersScore==21 and DealersScore==21):
            print("IT'S A TIE")
            print(f"PLAYER'S SCORE={PlayersScore}")
            print(f"DEALER'S SCORE={DealersScore}")
            print(f"DEALER'S CARDS={DealersCards}")
            money+=amt
            break;
        elif(PlayersScore==21):
            print("CONGRATULATIONS!! PLAYER HAS WON THE GAME!")
            print(f"PLAYER'S SCORE={PlayersScore}")
            print(f"DEALER'S SCORE={DealersScore}")
            print(f"DEALER'S CARDS={DealersCards}")
            money+=2*amt
            break;
        elif(DealersScore==21):
            print("UGHHHHHH!! PLAYER HAS LOST THE MATCH!")
            print(f"PLAYER'S SCORE={PlayersScore}")
            print(f"DEALER'S SCORE={DealersScore}")
            print(f"DEALER'S CARDS={DealersCards}")
            break;
        elif(PlayersScore>21 and DealersScore>21):
            print("IT'S A TIE")
            print(f"PLAYER'S SCORE={PlayersScore}")
            print(f"DEALER'S SCORE={DealersScore}")
            print(f"DEALER'S CARDS={DealersCards}")
            money+=amt
            break;
        elif(PlayersScore>21):
            print("UGHHHHHH!! PLAYER HAS LOST THE MATCH!")
            print(f"PLAYER'S SCORE={PlayersScore}")
            print(f"DEALER'S SCORE={DealersScore}")
            print(f"DEALER'S CARDS={DealersCards}")
            break;
        elif(DealersScore>21):
            print("CONGRATULATIONS!! PLAYER HAS WON THE GAME!")
            print(f"PLAYER'S SCORE={PlayersScore}")
            print(f"DEALER'S SCORE={DealersScore}")
            print(f"DEALER'S CARDS={DealersCards}")
            money+=2*amt
            break;
                                        
        print("What would you like to do?")
        print("H: HIT ME")
        print("S: STAND")
        print("\n")
        choice=''
        while (choice!='H' and choice!='S'):
            try:
                choice=input()
                choice=choice.upper()
                if(choice!='H' and choice!='S'):
                    print("Please Enter Valid Choice!")
            except:
                pass
    
        if (choice=='H'):
            PlayersCards.append(CardDeck.pop())
        else:
            if(PlayersScore==DealersScore):
                print("IT'S A TIE")
                print(f"PLAYER'S SCORE={PlayersScore}")
                print(f"DEALER'S SCORE={DealersScore}")
                print(f"DEALER'S CARDS={DealersCards}")
                money+=amt
                break;
            elif(PlayersScore>DealersScore):
                print("CONGRATULATIONS!! PLAYER HAS WON THE GAME!")
                print(f"PLAYER'S SCORE={PlayersScore}")
                print(f"DEALER'S SCORE={DealersScore}")
                print(f"DEALER'S CARDS={DealersCards}")
                money+=2*amt
                break;
            else:
                print("UGHHHHHH!! PLAYER HAS LOST THE MATCH!")
                print(f"PLAYER'S SCORE={PlayersScore}")
                print(f"DEALER'S SCORE={DealersScore}")
                print(f"DEALER'S CARDS={DealersCards}")
                break;
    choice2=''
    print(f"MONEY IN YOUR ACCOUNT= {money} Rs")
    while(choice2!='Y' and choice2!='N'):
        choice2=input("Would you like to play again?\n")
        choice2=choice2.upper()
        print("\n")
        if(choice2!='Y' and choice2!='N'):
            print("Enter a Valid Choice!")
            print("\n")
    if(choice2=='N'):
        renew="NO"
        print("THANK YOU FOR PLAYING!!!")
        print(f"PLEASE COLLECT YOUR BALANCE OF {money} Rs")
        print("HOPE TO SEE YOU SOON!!!")