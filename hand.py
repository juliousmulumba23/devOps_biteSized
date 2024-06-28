values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Hand:
    def __init__(self):
        self.playing_cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, single_card):
        self.playing_cards.append(single_card)
        self.value += values[single_card.rank]

        if single_card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        # IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        # THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
