class PlayerChips:
    def __init__(self):
        self.chips = 0
        self.bet = 0
        self.highest = 0
        self.lowest = 0
    
    def set_chips(self, chips):
        self.chips = chips
        self.update_stats()

    def set_chips_and_stats(self, chips):
        """
        Sets chips and both the highest and lowest stats to the value in parameter
        """
        self.chips = chips
        self.highest = chips
        self.lowest = chips
    
    def set_bet(self, bet):
        self.bet = bet
    
    # The game handles the multiplier, which determines how many times you win or lose your bet
    def process_bet(self, multiplier):
        self.chips += self.bet * multiplier
        self.update_stats()
    
    def update_stats(self):
        """
        Updates highest and lowest if the current chip counts "beats" one of those values
        """
        if self.chips > self.highest:
            self.highest = self.chips
        if self.chips < self.lowest:
            self.lowest = self.chips