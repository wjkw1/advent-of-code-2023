from src import utils


class Card:
    def __init__(self, line):
        stripped_line = line.split(": ")[1]
        self.winning_numbers = self.get_winning_numbers(stripped_line)
        self.hand = self.get_hand(stripped_line)

    def get_winning_numbers(self, line):
        return line.strip().split("| ")[0].strip().split()

    def get_hand(self, line):
        return line.split("| ")[1].split()

    def __repr__(self):
        return f"{self.__class__.__name__}(winning_numbers={self.winning_numbers}, hand={self.hand})"

    def add_to_score(self, current_score):
        """Increment the score as defined"""
        if current_score == 0:
            return 1
        return current_score * 2

    def calculate_score(self) -> int:
        """calculate our score for part 1"""
        score = 0
        for num in self.hand:
            if num in self.winning_numbers:
                score = self.add_to_score(score)
        return score


if __name__ == "__main__":
    # inputs = utils.read_file("src/day04/input-mini.txt")
    inputs = utils.read_file("src/day04/input.txt")

    pile_score = 0
    for line in inputs:
        card = Card(line)
        pile_score = pile_score + card.calculate_score()

    print(pile_score)
