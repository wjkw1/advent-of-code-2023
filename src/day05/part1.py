from src import utils


class Range:
    def __init__(self, start: int, length: int):
        self.start = start
        # subtract one from length to get the index end value
        self.end = start + (length -1)
        self.length = length

    def is_within_range(self, value: int):
        return self.start <= value <= self.end

    def get_index_of_value(self, value: int):
        # get the index of our value, returns None if doesn't exist
        if self.is_within_range(value):
            index = value - self.start
            return index
        else:
            return None

    def get_value_from_index(self, index: int):
        if 0 <= index < self.length:
            value = self.start + index
            return value
        return None

    def __repr__(self):
        return f"{self.__class__.__name__}(start={self.start}, end={self.end}, length={self.length})"


class Map:
    def __init__(self, map_type: str, map_list: list):
        self.map_type = map_type
        self.sources, self.dests = self._setup_map(map_list)

    def _setup_map(self, map_list: list) -> tuple:
        sources = []
        dests = []
        for map_line in map_list:
            dest, src, range_length = map_line.strip().split()
            sources.append(Range(int(src), int(range_length)))
            dests.append(Range(int(dest), int(range_length)))
        return sources, dests

    def get_destination(self, source_value: int):
        # loop through our range lists and check for matches
        for index, source_range in enumerate(self.sources):
            print(
                f"Value: {source_value}; Source: {source_range} ; Dest: {self.dests[index]}"
            )
            i = source_range.get_index_of_value(source_value)
            if i is not None:
                print(
                    f"{self.map_type} index found {i} with value: {self.dests[index].get_value_from_index(i)}"
                )
                return self.dests[index].get_value_from_index(i)

        # if we don't set the value, set to the source value
        return source_value

    def __repr__(self):
        return f"{self.__class__.__name__}(map_type={self.map_type}, sources={self.sources}, dests={self.dests})"


if __name__ == "__main__":
    # inputs = utils.read_file("src/day05/input-mini.txt")
    inputs = utils.read_file("src/day05/input.txt")

    # build up a list of maps, then give a function a seed and go map by map to find its end goal
    # replies on double newline at end of input to add final group to map 
    curr_map_type = ""
    curr_map_list = []
    maps = []
    for line in inputs[2:]:
        if len(line) > 0:
            if curr_map_type == "":
                curr_map_type = line.split()[0]
                continue
            curr_map_list.append(line.strip())
        else:
            curr_map = Map(curr_map_type, curr_map_list)
            maps.append(curr_map)
            curr_map_type = ""
            curr_map_list = []

    seeds = inputs[0].strip().split(": ")[1].split()
    locations = []
    for seed in seeds:
        source = seed
        # lets go on a journey through our maps
        for m in maps:
            source = m.get_destination(int(source))

        # The final source will be a location
        locations.append(source)
    print(f"Location: {min(locations)}")
