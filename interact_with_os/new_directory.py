import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if not os.path.isdir(directory):
    os.mkdir(directory)
  # Create the new file inside of the new directory
  with open(os.path.join(directory, filename),"w") as file:
    file.write("")

  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))
