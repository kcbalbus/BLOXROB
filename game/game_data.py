import json
from pieces import *

class GameData:
    def __init__(self):
        self.game_data = {
            "Easy": {
                "best_score": 0,
                "curr_score": 0,
                "board_setup": {
                    "Block1x1": [[0, 0], [0, 1], [3, 0], [3, 1], [1, 3], [2, 3], [1, 4], [2, 4]],
                    "Block2x1": [[0, 3], [3, 3]],
                    "Block1x2": [[1, 2]],
                    "Block2x2": [[1, 0]]
                },
                "board_state": {
                    "Block1x1": [[0, 0], [0, 1], [3, 0], [3, 1], [1, 3], [2, 3], [1, 4], [2, 4]],
                    "Block2x1": [[0, 3], [3, 3]],
                    "Block1x2": [[1, 2]],
                    "Block2x2": [[1, 0]]
                },
            },
            "Medium": {
                "best_score": 0,
                "curr_score": 0,
                "board_setup": {
                    "Block1x1": [[0, 2], [3, 2], [1, 3], [2, 3], [1, 4], [2, 4]],
                    "Block2x1": [[0, 0], [3, 0], [0, 3], [3, 3]],
                    "Block1x2": [],
                    "Block2x2": [[1, 0]]
                },
                "board_state": {
                    "Block1x1": [[0, 2], [3, 2], [1, 3], [2, 3], [1, 4], [2, 4]],
                    "Block2x1": [[0, 0], [3, 0], [0, 3], [3, 3]],
                    "Block1x2": [],
                    "Block2x2": [[1, 0]]
                },
            },
            "Hard": {
                "best_score": 0,
                "curr_score": 0,
                "board_setup": {
                    "Block1x1": [[1, 3], [2, 3], [1, 4], [2, 4]],
                    "Block2x1": [[0, 0], [3, 0], [0, 3], [3, 3]],
                    "Block1x2": [[1, 2]],
                    "Block2x2": [[1, 0]]
                },
                "board_state": {
                    "Block1x1": [[1, 3], [2, 3], [1, 4], [2, 4]],
                    "Block2x1": [[0, 0], [3, 0], [0, 3], [3, 3]],
                    "Block1x2": [[1, 2]],
                    "Block2x2": [[1, 0]]
                },
            }
        }

    def save_lvl(self, difficulty, blocks_group, moves):
        for block_type in self.game_data[difficulty]["board_state"]:
            self.game_data[difficulty]["board_state"][block_type].clear()

        for block in blocks_group:
            self.game_data[difficulty]["board_state"][block.__class__.__name__].append([block.get_x(), block.get_y()])

        self.game_data[difficulty]["curr_score"] = moves

    def load_lvl(self, difficulty):
        return (self.create_blocks(self.game_data[difficulty]["board_state"], difficulty), self.game_data[difficulty]["curr_score"])

    def restart_lvl(self, difficulty):
        return (self.create_blocks(self.game_data[difficulty]["board_setup"], difficulty), 0)


    def restart_lvl_state(self, difficulty):
        self.game_data[difficulty]["board_state"] = self.game_data[difficulty]["board_setup"]
        self.game_data[difficulty]["curr_moves"] = 0

    def create_blocks(self, blocks_dict, difficulty):
        blocks_list = []
        for block in blocks_dict["Block1x1"]:
            blocks_list.append(Block1x1(block[0], block[1], difficulty))
        for block in blocks_dict["Block2x1"]:
            blocks_list.append(Block2x1(block[0], block[1], difficulty))
        for block in blocks_dict["Block1x2"]:
            blocks_list.append(Block1x2(block[0], block[1], difficulty))
        for block in blocks_dict["Block2x2"]:
            blocks_list.append(Block2x2(block[0], block[1], difficulty))

        return blocks_list


    def save_best_score(self, difficulty, moves):
        best_score = self.game_data[difficulty]["best_score"]
        if moves < best_score or best_score==0:
            self.game_data[difficulty]["best_score"] = moves
            return True
        return False

    def load_best_scores(self):
        best_scores = {}
        for difficulty in self.game_data:
            best_scores[difficulty] = self.game_data[difficulty]["best_score"]

        return best_scores

    def save_data(self):
        with open("game_data.json", "w") as file:
            json.dump(self.game_data, file)

    def load_data(self):
        try:
            with open("game_data.json", "r") as file:
                self.game_data = json.load(file)
        except FileNotFoundError:
            pass











