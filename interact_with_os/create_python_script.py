import os

def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
  filesize = str(os.stat(filename).st_size)
  return(filesize)

print(create_python_script("program.py"))
