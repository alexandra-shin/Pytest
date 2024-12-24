class ReaderClass:

    '''
    ReaderClass helps to record and read data from the specified .txt file.
    Patterns are used to recognize which particular value should be recorded/retrieved.
    '''

    file_path = "yourPath/example.txt"
    isNoMatch = True

    @staticmethod
    def record(self, value_to_record: str, pattern: str):
        try:
            with open(self.file_path, "r") as file: 
                lst = file.readlines()
                for line in lst:
                    if line.startswith(pattern): 
                        self.isNoMatch = False
                        lst.append(value_to_record)
                        lst.remove(line)
                if self.isNoMatch:
                    lst.append(value_to_record)
            with open(self.file_path, "w") as file:
                for newLine in lst:
                    file.write(newLine)
            print("Your recorded value is: " + value_to_record)        
        except FileNotFoundError:
            with open(self.file_path, "w") as file:
                file.write(value_to_record)
            print("Your recorded value is: " + value_to_record)

    @staticmethod
    def read(self, pattern: str) -> str:
        try:
            with open(self.file_path, "r") as file: 
                lst = file.readlines()
                for line in lst:
                    if line.startswith(pattern): 
                        newLine = line[3:10]    # example
                        return newLine
        except FileNotFoundError:
            print("File 'example.txt' has been not found.")              
