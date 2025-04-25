"""f = open('demo.txt', 'w')
f.write("Hola como estas "
        "What are you doing? "
        "Where are you going? ")
f.close()"""

f = open('demo.txt', 'r')
y = f.read(5)
print(y)
f.close()

"""f = open("demo.txt", 'a')
f.write("Have you done your homework! "
        "Let's go play some games.")
f.close()"""

f = open('demo.txt', 'r')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline(), end='')
print(f.readline())
f.seek(0)
print(f.readlines())
f.seek(69)                     # moves cursor to particular index
print(f.tell())                # tells the position of cursor
f.close
