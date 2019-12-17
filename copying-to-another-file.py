from sys import argv

script, filename, filename2 = argv

print(f"We're goign to copy the contents of {filename} to {filename2}")
print(f"First let's write to {filename}")

file = open(filename,"w+")
file.write(input("Please enter the contents of the file:\n"))

file = open(filename,"r")
contents = file.read()
print(f"Here are the contents of {filename}:\n",contents)

file2 = open(filename2,"w")
file2.write(contents)

file2 = open(filename2,"r")
print(f"How here are the contents of {filename2}:\n",file2.read())

file1.close()
file2.close()
