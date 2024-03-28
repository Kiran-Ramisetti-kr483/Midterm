import pandas as pd

class claculation_history:
    def __init__(self):
        self.history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def add_entry(self, operation, operand1, operand2, result):
        new_entry = pd.DataFrame({'Operation': [operation], 
                                  'Operand1': [operand1], 
                                  'Operand2': [operand2], 
                                  'Result': [result]})
        if self.history.empty:
            self.history = new_entry
        else:
            self.history = pd.concat([self.history, new_entry], ignore_index=True, sort=False)

    def display_history(self):
        print("Calculation History:")
        print(self.history)

    def save_history(self, filename):
        self.history.to_csv(filename, index=False)

    def load_history(self, filename):
        try:
            self.history = pd.read_csv(filename)
        except FileNotFoundError:
            print("History file not found.")

    def clear_history(self):
        self.history = pd.DataFrame(columns=['Operation', 'Operand1', 'Operand2', 'Result'])

    def delete_entry(self, index):
        if index < len(self.history):
            self.history.drop(index, inplace=True)
            print("Entry deleted successfully.")
        else:
            print("Invalid index.")
