import random

class Cards():
    def __init__(self):
        self.dealer_cards = []
        self.player_cards = []
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        

        

    def dealCards(self):
        self.player = self.findTotalPlayer()
        self.dealer = self.findTotalDealer()
        while len(self.dealer_cards) != 2:
            self.dealer_cards.append(random.choice(self.deck))
            if len(self.dealer_cards) == 2:
                print("Dealer has: ? &", self.dealer_cards[1])
                # self.dealer = self.findTotalDealer()
                # if self.dealer == 21:
                #     print("\nDealer has BlackJack.\n Better luck next time.\n")


        while len(self.player_cards) != 2:
            self.player_cards.append(random.choice(self.deck))
            if len(self.player_cards) == 2:
                print("You have:", self.player_cards)
                self.player = self.findTotalPlayer()
                if self.player == 21:
                    print("\nBlackJack! You Win!\n")
                    break
                
                    
                

# bug here... cant figure out how to make the aces 11 or 1 for the entirety of the loop

    def findTotalPlayer(self):
        self.total = 0
        for card in self.player_cards:
            if card == 'A':
                card = self.player_cards[-1]
            
        while True:
            for i in self.player_cards:
                if i in range(1, 11):
                    self.total += i
                elif i == 'J':
                    self.total += 10
                elif i == 'Q':
                    self.total += 10
                elif i == 'K':
                    self.total += 10
                elif i == 'A':
                    if self.total <= 10:
                        self.total += 11
                    else:
                        self.total += 1   
                else:
                    break
            return self.total
    
        
    # def displayScoreboard(self):
    #     self.p_wins = 0
    #     self.d_wins = 0
    #     self.p_wins += self.player_wins
    #     self.d_wins += self.dealer_wins
    #     self.scoreboard = f"Dealer --> {self.d_wins} | {self.p_wins} <-- Player \n"
    #     print(self.scoreboard)


    def findTotalDealer(self):
        self.total = 0
        
        while True:
            for i in self.dealer_cards:
                if i in range(1, 11):
                    self.total += i
                elif i == 'J':
                    self.total += 10
                elif i == 'Q':
                    self.total += 10
                elif i == 'K':
                    self.total += 10
                elif i == 'A':
                    if self.total <= 10:
                        self.total += 11
                    else:
                        self.total += 1   
                else:
                    break
            return self.total
            


    def run(self):
        self.player_wins = 0
        self.dealer_wins = 0
        self.player = self.findTotalPlayer()
        self.dealer = self.findTotalDealer()
        self.win_1 = "\nCongratulations, you have beaten the dealer\n"
        self.win_2 = "\nUnfortunately, the dealer has you beat\n"
        self.bust = "BUSTED\n"
        self.draw = "\n Even match. play again. \n"

        while True:
                if self.player == 21:
                    print("The dealer has: ", self.dealer_cards, "\nThats 21! You Win!\n", self.win_1, "\n")
                    
                    
                    break
                elif self.player > 21:
                    print("You have", self.bust, self.win_2)
                    
                    
                    break
                elif self.dealer > 21:
                    print("Dealer is", self.bust, self.win_1)
                    
                    break
                elif self.player > self.dealer:
                    print("The dealer has: ", self.dealer_cards, "\n \nDealer Total: ", self.dealer, "---", "Player Total: ", self.player)
                    print(self.win_1)
                    
                    break
                elif self.player < self.dealer:
                    print("The dealer has: ", self.dealer_cards, "\n \nDealer Total: ", self.dealer, "---", "Player Total: ", self.player)
                    print(self.win_2)
                    
                    break
                elif self.player == self.dealer:
                    
                    print("The dealer has: ", self.dealer_cards, "\n \nDealer Total: ", self.dealer, "---", "Player Total: ", self.player)
                    print(self.draw)
                    
                    break
                else:
                    break
            

    def dealerHit(self):
        self.dealer = self.findTotalDealer()
        while True:
            if self.dealer < 16:
                print("Dealer has: ", self.dealer_cards)
                print("The dealer is now hitting... ")
                self.dealer_cards.append(random.choice(self.deck))
                print(self.dealer_cards[:-1], "+", self.dealer_cards[-1])
                self.dealer = self.findTotalDealer()
            else: 
                break


        
    def hit(self):
        self.bust = "BUSTED"
        self.player = self.findTotalPlayer()
        self.dealer = self.findTotalDealer()
        while True:
            self.action = input("STAY or HIT? ")
            if self.action.lower() == 'hit':
                self.player_cards.append(random.choice(self.deck))
                self.player = self.findTotalPlayer()
                if self.player > 21:
                    print("+", self.player_cards[-1], "\n", self.bust)
                    break
                else:
                    print("You now have: ", self.player_cards)
            else:
                break
    
            



while True:
    me = Cards()
    play = input("Play BlackJack? yes or no --> ")
    if play == 'yes':
        
        me.dealCards()
        me.hit()
        me.dealerHit()
        me.run()
    else:
        break