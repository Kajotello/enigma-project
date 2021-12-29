from PySide2.QtCore import QAbstractTableModel, Qt


class ConifgTableModel(QAbstractTableModel):
    def __init__(self, data=None) -> None:
        super(ConifgTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Name", "Position", "Ring")[section]
        else:
            return f"{section+1}"


class StepsTableModel(QAbstractTableModel):
    def __init__(self, data=None) -> None:
        super(StepsTableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Vertical:
            return ("Input", "Plugboard Encryption", "3rd Rotor Encryption",
                    "2nd Rotor Encryption", "1st Rotor Encryption",
                    "reflector Encryption", "1st Rotor Encryption",
                    "2nd Rotor Encryption", "3rd Rotor Encryption",
                    "Plugboard Encryption", "Output")[section]
