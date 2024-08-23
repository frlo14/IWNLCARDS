import random
import itertools

class Card:
    def __init__(self, suit, number, priority=0):
        self.suit = suit
        self.number = number
        self.priority = priority

    def getNumber(self):
        return self.number

    def __repr__(self):
        return f"{self.number} of {self.suit} (Priority: {self.priority})"

    @staticmethod
    def generateCards():
        deck = []
        suits = ["gold", "clubs", "swords", "cups"]
        numbers = range(1, 11)  
        for suit in suits:
            for number in numbers:
                deck.append(Card(suit, number))
        return deck

class Game:
    def __init__(self):
        self.deck = Card.generateCards()
        self.table = []
        self.playerHand = []
        self.opponentHand = []
        self.turn = 1

    def shuffleDeck(self):
        random.shuffle(self.deck)
    
    def dealCards(self):
        self.shuffleDeck()
        self.playerHand = [self.deck.pop() for i in range(3)]
        self.opponentHand = [self.deck.pop() for i in range(3)]
        if self.turn == 1:
            self.table = [self.deck.pop() for i in range(4)]

    def addUpFifteen(self, numbers):
        return [combo for r in range(1, len(numbers) + 1) 
                for combo in itertools.combinations(numbers, r) 
                if sum(combo) == 15]

    def findBestMove(self):
        bestMove = None
        bestScore = 0

        for card in self.playerHand:
            possibleMoves = []
            tableWCard = [card.getNumber()] + [tableCard.getNumber() for tableCard in self.table]
            combos = self.addUpFifteen(tableWCard)
            
            combos = [combo for combo in combos if card.getNumber() in combo]

            for combo in combos:
                moveScore = len(combo)  
                
                if moveScore > bestScore:
                    bestScore = moveScore
                    bestMove = (card, combo)

        if bestMove:
            bestMove[0].priority = 1  
            return bestMove[0], bestMove[1]  

        return None

game = Game()
game.dealCards()
bestMove, comboPicked = game.findBestMove()
print("Player's Hand:", game.playerHand)
print("Table:", game.table)
if bestMove:
    print("play", bestMove, "and pick up", comboPicked)
else:
    print("must put down a card")

#continue game and use player inputs
#fix which move is best as opposed to which picks up the most cards. could find best move for each category then assign a weight to them, largest weight is favoured
#consider which cards have already been played
