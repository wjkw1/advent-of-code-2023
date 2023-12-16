from src import utils

def multiply_list(num_wins):
    result = 1
    for x in num_wins:
        result = result * x
    return result


class Race:
    def __init__(self, max_time: int, dist_to_beat: int):
        self.max_time = max_time
        self.dist_to_beat = dist_to_beat

    def __repr__(self):
        return f"{self.__class__.__name__}(max_time={self.max_time}, dist_to_beat={self.dist_to_beat})"

    def _get_destination(self, speed: int):
        # given a speed, how far do we get
        time_to_race = self.max_time - speed
        if time_to_race <= 0:
            return None
        return speed * time_to_race

    def get_number_of_ways_to_win(self):
        win_count = 0
        for speed in range(self.max_time):
            if self._get_destination(speed) > self.dist_to_beat:
                win_count += 1
        return win_count


if __name__ == "__main__":
    # inputs = utils.read_file("src/day06/input-mini.txt")
    inputs = utils.read_file("src/day06/input.txt")
    times = inputs[0].split()[1:]
    distances = inputs[1].split()[1:]

    num_wins_list = []
    for index, time in enumerate(times):
        curr_race = Race(int(time), int(distances[index]))
        num_wins_list.append(curr_race.get_number_of_ways_to_win())

    margin_of_error = multiply_list(num_wins_list)

    print(margin_of_error)
