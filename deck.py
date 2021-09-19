import random

class Deck:
    def __init__(self, num_decks: int, penetration: float = 0):
        """
        params:
        num_decks: Number of decks to shuffle in
        penetration: Portion of the deck not to be dealt before reshuffling
        """
        self.num_decks = num_decks
        self.reshuffle()
        # Penetration is stored to min_cards to ease future referencing
        self.min_cards = penetration * self.num_cards
    
    def draw_card(self) -> int:
        """
        Draws a random card from the deck, weighed according to how many are left, removing the
        drawn card from the deck. Returns between 1 and 13, 1 is Ace, 2 through 10 are their
        literal value, then 11/12/13 for J/Q/K. Reshuffles if under the min_cards threshold after
        drawing.
        """
        card_drawn_number = random.randint(0, self.num_cards - 1)
        card_tally = 0
        card_index = 0
        while True:
            card_tally += self.card_array[card_index]
            if card_drawn_number < card_tally:
                self.num_cards -= 1
                self.card_array[card_index] -= 1
                if self.num_cards <= self.min_cards:
                    self.reshuffle()
                return card_index + 1
            card_index += 1
    
    def reshuffle(self):
        """
        Initialises the card_array to its default values and num_cards.
        """
        self.num_cards = self.num_decks * 52
        self.card_array = [self.num_decks * 4] * 13
    
    def print_deck(self):
        """
        Prints out the remaining cards in the deck. Jack chosen for the 10 value for aesthetics.
        """
        output = f"Cards left: {self.num_cards}\nA: {self.card_array[0]}\n"
        card_index = 1
        while card_index <= 8:
            output += f"{card_index+1}: {self.card_array[card_index]}\n"
            card_index += 1
        output += f"T: {self.card_array[9]}\nJ: {self.card_array[10]}\nQ: {self.card_array[11]}\nK: {self.card_array[12]}\n"
        print(output)

if __name__ == '__main__':
    deck = Deck(2, 0.4)
    for i in range(52):
        deck.draw_card()
    deck.print_deck()