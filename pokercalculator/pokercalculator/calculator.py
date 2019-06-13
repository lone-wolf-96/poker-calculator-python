from final_class import final


@final
class Calculator:

    def __init__(self, filePath):
        self.calculate(filePath)

    def calculate(self, filePath):
        print(f"{filePath}\n")

    def print_results(self, filePath):
        print(f"{filePath}\n")
        return True
