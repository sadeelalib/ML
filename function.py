class ResourceManager:
    def __init__(self, file_name):
        # Constructor: Open the file for writing
        self.file = open(file_name, 'w')
        print(f"File {file_name} opened")

    def write_to_file(self, data):
        # Method to write data to the file
        self.file.write(data)

    def __del__(self):
        # Destructor: Close the file
        self.file.close()
        print("File closed")

# Creating and using the ResourceManager object
resource = ResourceManager("example_file.txt")
resource.write_to_file("This is a test.")
# Deleting the object to trigger the destructor
del resource
