import morse

def help():
    print("morse 'string' - convert a string into morse code")
    print("string 'morse' - translate a morse code sequence")

print(r"""
 ███▄ ▄███▓ ▒█████   ██▀███    ██████ ▓█████ 
▓██▒▀█▀ ██▒▒██▒  ██▒▓██ ▒ ██▒▒██    ▒ ▓█   ▀ 
▓██    ▓██░▒██░  ██▒▓██ ░▄█ ▒░ ▓██▄   ▒███   
▒██    ▒██ ▒██   ██░▒██▀▀█▄    ▒   ██▒▒▓█  ▄ 
▒██▒   ░██▒░ ████▓▒░░██▓ ▒██▒▒██████▒▒░▒████▒
░ ▒░   ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒░ ░
░  ░      ░  ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒  ░ ░ ░ ░  ░
░      ░   ░ ░ ░ ▒    ░░   ░ ░  ░  ░     ░   
       ░       ░ ░     ░           ░     ░  ░
""")
help()
print()

while True:
    command = input(">> ")

    if command == "exit":
        print("Bye bye!")
        break

    if command == "help":
        help()
        continue

    if command[:6] == "morse ":
        print(morse.convert(command[6:]))
        continue

    if command[:7] == "string ":
        print(morse.translate(command[7:]))
        continue

    print("... ?")