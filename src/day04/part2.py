from src import utils


class Card:
    def __init__(self, line):
        self.copies = 1
        self.card_name, stripped_line = line.split(": ")
        self.winning_numbers = self.get_winning_numbers(stripped_line)
        self.hand = self.get_hand(stripped_line)

    def get_winning_numbers(self, line):
        return line.strip().split("| ")[0].strip().split()

    def get_hand(self, line):
        return line.split("| ")[1].split()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}(card_name={self.card_name}, "
            f"winning_numbers={self.winning_numbers}, hand={self.hand}, "
            f"index={self.get_index()}, copies={self.get_copies()})"
        )

    def get_matches(self) -> int:
        matches = 0
        for num in self.hand:
            if num in self.winning_numbers:
                matches += 1
        return matches

    def increment_copies(self) -> None:
        self.copies += 1

    def get_copies(self) -> int:
        return self.copies

    def get_index(self):
        return int(self.card_name.strip().split()[1]) - 1

    def get_next_indices(self) -> list:
        index = self.get_index()
        next_indices = []
        for match in range(self.get_matches()):
            index += 1
            next_indices.append(index)
        return next_indices


if __name__ == "__main__":
    # inputs = utils.read_file("src/day04/input-mini.txt")
    inputs = utils.read_file("src/day04/input.txt")

    # setup our pile
    pile = []
    for line in inputs:
        card = Card(line)
        pile.append(card)

    total_copies = 0
    # loop through pile, updating card copies
    for card in pile:
        total_copies += card.get_copies()
        if card.get_copies() == 0:
            print(f"\n\nWe finish on this card: {card}")
            break
        else:
            print(card)

        # We need to get all of the next card indexes
        # and increment those copies based on the number of copies our current card has
        for next_index_match in card.get_next_indices():
            for copy in range(card.get_copies()):
                # check if next_index_match is within our list
                pile[next_index_match].increment_copies()
    print(total_copies)
