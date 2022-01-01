from enigma_classes.functions import to_number


class Plugboard:

    """Represent plugboard of machine"""

    def __init__(self, connections) -> None:
        self._connections_table = connections
        self._connections_str = ""
        self._connections = {}
        for element in connections:
            first_letter, second_letter = element
            self._connections_str += first_letter+second_letter+""
            first_letter = to_number(first_letter)
            second_letter = to_number(second_letter)
            self._connections[first_letter] = second_letter
            self._connections[second_letter] = first_letter

    @property
    def connections_table(self):
        return self._connections_table

    @property
    def connections(self):
        return self._connections

    @property
    def connections_str(self):
        return self._connections_str

    def __str__(self):
        return self.connections_str

    def code(self, ASCII_letter):
        return self.connections.get(ASCII_letter, ASCII_letter)
