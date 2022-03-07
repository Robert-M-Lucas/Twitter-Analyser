import pandas
import Operations as op


class Axis:
    axis_id: int

    def __init__(self, axis_id):
        self.axis_id = axis_id
        self.starting_value = "Likes"
        self.operations = []
        self.string = ""
        self.load()

    def load(self):
        try:
            with open("data/AXIS_" + str(self.axis_id) + ".txt", "r") as f:
                data = f.read().split("\n")
                self.starting_value = data[0]
                self.operations = data[1:]
        except FileNotFoundError:
            pass

    def save(self):
        with open("data/AXIS_" + str(self.axis_id) + ".txt", "w") as f:
            text = ""
            text += self.starting_value
            text += "\n"
            for operation in self.operations:
                text += operation + "\n"
            text = text[:-1]
            f.write(text)

    def get_string(self):
        self.string = self.starting_value
        for i, operation in enumerate(self.operations):
            if i % 2 == 0:
                self.string += " " + op.Operations[operation][1]
            else:
                self.string += " " + operation
                self.string += ";"

    def get_list(self, df: pandas.DataFrame) -> list:
        true_starting_value = op.Values[self.starting_value][0]
        full_list = []
        for i in range(len(df[true_starting_value])):
            x = df[true_starting_value][i]

            for j in range(int(len(self.operations) / 2)):
                second_value = self.operations[j * 2 + 1]
                if second_value in op.Values.keys():
                    second_value = df[op.Values[second_value][0]][i]
                else:
                    second_value = float(second_value)

                x = op.Operations[self.operations[j * 2]][0](x, second_value)

            full_list.append(x)
        return full_list
