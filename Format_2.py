print("\n{}, this is how format is defined in python.\n".format("Format:"))

str = "This article is written in {}"
print(str.format("python"))

print("\n Hello, I am {} years old !".format(25))

print("\nHi ! My name is {} and I am {} years old".format("Cena", 28))

# The values passed as parameters
# are replaced in order of their entry
print("\nThis is {} {} {} {}"
      .format("Peter", "Robert", "Tipu", "Motu"))

print("{0} loves {1}!!".format("Wahed", "You"))

print("\nEvery {} should know the use of {} {} programming and {}"
    .format("programmer", "Open", "Source", "Operating Systems"))

print("\n ***********this is with indexing************")
print("Every {3} should know the use of {1} {2} programming and {0}"
        .format("programmer", "Open", "Source", "Operating Systems"))

# Keyword arguments are called
# by their keyword name
print("\n{gfg} is a {0} science portal for {1}"
.format("computer", "geeks", gfg ="GeeksforGeeks"))

my_string = "{}, is a {} {} science portal for {}"
print(my_string.format("GeeksforGeeks", "Computer", "geeks"))
# isme aur ek element pass kare to ata

