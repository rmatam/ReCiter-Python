from time import gmtime, strftime

target = open("test" + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + ".txt", 'w')

print("Truncating the file.  Goodbye!")
target.truncate()

target.write("test")

print("And finally, we close it.")
target.close()
