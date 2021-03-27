import random

suits = ('红心', '方块', '黑桃', '梅花')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}
playing = True
global totals
totals = 1000000

class Card:    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank        
    def __str__(self):
        return self.suit + self.rank
    
class Deck:    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))                               
    def shuffle(self):
        random.shuffle(self.deck)        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Hand:    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
class Chips:    
    def __init__(self):
        self.total = totals
        self.bet = 0        
    def win_bet(self):
        self.total += self.bet    
    def lose_bet(self):
        self.total -= self.bet
        
def take_bet(chips):
    while True:
        chips.bet = int(input("你要赌多少个冰激凌(1-1000000的整数)："))
        if  chips.bet > chips.total:
            print("你输入的数量不对哦！不能超过自己的冰激凌数：", chips.total)
            continue
        else:
            break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck, hand):
    global playing    
    while True:
        x = input("你要停牌还是拿牌?输入'h'表示拿牌,输入's'表示停牌:")        
        if x == 'h':
            hit(deck,hand)
        elif x == 's':
            print("玩家停牌,电脑继续玩。")
            playing = False
        else:
            print("请输入正确的字母。")
            continue
        break
    
def show_some(player, dealer):
    print("\n电脑的牌:")
    print(" <隐藏的牌>")
    print('', dealer.cards[1])  
    print("\n玩家的牌:", *player.cards, sep='\n ')
    
def show_all(player, dealer):
    print("\n电脑的牌:", *dealer.cards, sep='\n ')
    print("电脑的牌 =",dealer.value)
    print("\n玩家的牌:", *player.cards, sep='\n ')
    print("玩家的牌 =",player.value)
    
def player_busts(chips):
    print("玩家爆牌!")
    chips.lose_bet()

def player_wins(chips):
    print("玩家赢了!")
    chips.win_bet()

def dealer_busts(chips):
    print("电脑爆牌!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("电脑赢了!")
    chips.lose_bet()
    
def push():
    print("玩家和电脑平了！")
    

while True:
    print('欢迎来玩黑杰克游戏! 尽可能接近21点，但不要超过它了！\n\
    电脑会一直拿牌，直到17点。 A可以是1点或11点。')    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips = Chips()  
    
    take_bet(player_chips)
    
    show_some(player_hand, dealer_hand)
    
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)        
        if player_hand.value > 21:
            player_busts(player_chips)
            show_all(player_hand, dealer_hand)
            break
    
    if player_hand.value <= 21:        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)            
        show_all(player_hand, dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()

 
    print("\n剩余冰激凌数:", player_chips.total)
    totals = player_chips.total
    if totals == 0:
        print("冰激凌用光啦，游戏结束！")
        break
    new_game = input("你还想再玩一局吗?输入'y'表示继续，输入'n'表示结束:")
    if new_game == 'y':
        playing = True
        continue
    elif new_game == 'n':
        print("谢谢惠顾!")
        break
    else:
        print("输入错误,游戏结束！")
        break
