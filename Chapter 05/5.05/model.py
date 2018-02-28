"""
Code illustration: 5.05

@Tkinter GUI Application Development Blueprints
"""


class Model:

    def __init__(self):
        self.__play_list = []

    @property
    def play_list(self):
        return self.__play_list

    def get_file_to_play(self, file_index):
        return self.__play_list[file_index]

    def clear_play_list(self):
        self.__play_list.clear()

    def add_to_play_list(self, file_name):
        self.__play_list.append(file_name)

    def remove_item_from_play_list_at_index(self, index):
        del self.__play_list[index]
