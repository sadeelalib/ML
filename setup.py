from cx_Freeze import setup, Executable

# Replace 'main.py' with your actual script name
script_name = "main.py"

# Define the executables
executables = [Executable(script_name)]

# Define options to include packages and data files
build_options = {
    "packages": ["eel"],  # Include the eel package
    "include_files": ["www"],  # Include the web folder
}

# Setup configuration
setup(
    name="YourAppName",
    version="1.0",
    description="A simple eel application",
    options={"build_exe": build_options},
    executables=executables,
)
