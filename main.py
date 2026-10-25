import morse

def help():
    print("encode 'string' - string to morse code")
    print("decode 'morse'  - morse code to string")

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

    if command[:7] == "encode ":
        print(morse.convert(command[7:]))
        continue

    if command[:7] == "decode ":
        print(morse.translate(command[7:]))
        continue

    print("... ?")
