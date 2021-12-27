from functions import to_number


class Plugboard:

    """Represent plugboard of machine"""

    def __init__(self, connections) -> None:
        self._connections = {}
        for element in connections:
            first_letter, second_letter = element
            first_letter = to_number(first_letter)
            second_letter = to_number(second_letter)
            self._connections[first_letter] = second_letter
            self._connections[second_letter] = first_letter

    @property
    def connections(self):
        return self._connections

    def code(self, ASCII_letter):
        return self.connections.get(ASCII_letter, ASCII_letter)
