class PlayerCards:
    def __init__(self):
        self.reset()
    
    def reset(self):
        """
        Resets the player to their initial state.
        """
        self.count = 0
        self.soft = False
        self.can_double = True
        self.can_split = False
        self.first_card = 0
    
    def add_card(self, card):
        """
        Adds a card to the player's hand, updating all the flags accordingly
        """
        # This basically means "the previous card was the 2nd so you can't double/split anymore"
        if self.can_double and self.get_card_value(self.first_card) != self.count:
            self.can_double = False
            self.can_split = False
        # This is the second card and it's the same as the first, you can now split!
        if self.can_double and self.first_card == card:
            self.can_split = True
        if self.first_card == 0:
            self.first_card = card
        if card == 1:
            self.soft = True
        self.count += self.get_card_value(card)
        # Unsoften if you have an Ace worth 11 and it would make you bust
        if self.count > 21 and self.soft:
            self.soft = False
            self.count -= 10
    
    def get_card_value(self, card):
        """
        Get the value of the card for the purposes of the count.
        """
        if card >= 10:
            return 10
        if card == 1:
            return 11
        return card
    
    def pretty_print(self):
        """
        Prints all the flags (except first_card since it should never matter outside of its
        specific use case for splitting), nicely formatted
        """
        output = "Count: "
        if self.soft:
            output += "S"
        output += str(self.count)
        if self.can_double:
            output += ", can double"
        if self.can_split:
            output += ", can split"
        print(output)

if __name__ == '__main__':
    test = PlayerCards()
    test.add_card(6)
    test.add_card(8)
    test.pretty_print() # 14, can double
    test.add_card(3)
    test.pretty_print() # 17

    test.reset()
    test.add_card(7)
    test.add_card(7)
    test.pretty_print() # 14, can double, can split
    test.add_card(1)
    test.pretty_print() # 15

    test.reset()
    test.add_card(12)
    test.add_card(11)
    test.pretty_print() # 20, can double

    test.reset()
    test.add_card(1)
    test.add_card(3)
    test.pretty_print() # S14, can double
    test.add_card(7)
    test.pretty_print() # S21
    test.add_card(6)
    test.pretty_print() # 17