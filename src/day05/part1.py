import json
from src import utils

# TODO don't use a map, store a list of starts & ends (ranges), and search between that number > or < 

class Map:
    def __init__(self, map_type: str, map_list: list):
        self.map_type = map_type
        self.map_dict: dict = self._setup_map(map_list)

    def _setup_map(self, map_list: list):
        map_dict = {}
        for mapping in map_list:
            new_dict = self._get_map_parts(mapping)
            map_dict = {**map_dict, **new_dict}
        return map_dict

    def _get_map_parts(self, mapping: str):
        dest, src, range_length = mapping.strip().split()
        new_dict = {}
        for _ in range(int(range_length)):
            new_dict[f"{src}"] = dest
            src: str = str(float(src) + 1)
            dest: str = str(float(dest) + 1)
        return new_dict

    def __repr__(self):
        return f"{self.__class__.__name__}(map_type={self.map_type}, map_dict={json.dumps(self.map_dict)})"

    def get_destination(self, _source: str) -> str:
        # Any source numbers that aren't mapped correspond to the same destination number
        return self.map_dict.get(_source, _source)


if __name__ == "__main__":
    # inputs = utils.read_file("src/day05/input-mini.txt")
    inputs = utils.read_file("src/day05/input.txt")

    # build up a list of maps, then give a function a seed and go map by map to find its end goal
    curr_map_type = ""
    curr_map_list = []
    maps = []
    for line in inputs[2:]:
        if len(line) > 0:
            if curr_map_type == "":
                curr_map_type = line.split()[0]
                continue
            curr_map_list.append(line.strip())
            print(line)
        else:
            curr_map = Map(curr_map_type, curr_map_list)
            maps.append(curr_map)
            curr_map_type = ""
            curr_map_list = []
            print("<skip this line>")

    seeds = inputs[0].strip().split(": ")[1].split()
    locations = []
    for seed in seeds:
        source = seed
        # lets go on a journey through our maps
        for m in maps:
            source = m.get_destination(source)

        # The findal source will be a location
        locations.append(source)
    print(min(locations))
