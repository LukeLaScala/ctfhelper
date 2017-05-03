#!/usr/bin/python
import sys
import base64

if len(sys.argv) < 2:
    print("Usage: ctftool [-d | -e] [rot[0-25] | rot | base64 | b64] -i 'your input'")
    print('''
    -d for decryption
    -e for encryption

    rot
        rot for all rotations
            ex: ctftool -d rot -i WBJyf
        rot[num] for a specific rotation
            ex: ctftool -d rot4 -i WBJyF

        note that -e and -d are identical for rot

    base64
        ex: ctftool -d b64 -i bHVrZWxhc2NhbGE=
            ctftool -e b64 -i lukelascala
    ''')

if sys.argv[2] == "base64" or sys.argv[2] == "b64":

    if '-i' in sys.argv:
        if "-d" in sys.argv:
            print(base64.b64decode(' '.join(sys.argv[4:])))
        elif "-e" in sys.argv:
            print(base64.b64encode(' '.join(sys.argv[4:])))
    else:
        lines = []
        while True:
            try:
                line = raw_input()
            except EOFError:
                break
            if line == '':
                break
            lines.append(line)

        text = '\n'.join(lines)
        if "-d" in sys.argv:
            print(base64.b64decode(text))
        elif "-e" in sys.argv:
            print(base64.b64encode(text))

#not too easy to read but it gets the job done
if "rot" in sys.argv[2]:
    if '-i' in sys.argv:
        if sys.argv[2] == 'rot':
            for x in range(26):
                print('ROT ' + str(x) + ': ' +''.join([chr((((ord(char) - 65) % 26) + x) % 26 + 65) if 90 >= ord(char) >= 65 else chr((((ord(char) - 97) % 26) + x) % 26 + 97) if 97 <= ord(char) <= 122 else char for char in ' '.join(sys.argv[4:])]))
        else:
            print('ROT ' + str(sys.argv[2][3:]) + ': ' + ''.join([chr((((ord(char) - 65) % 26) + int(sys.argv[2][3:])) % 26 + 65) if 90 >= ord(char) >= 65 else chr((((ord(char) - 97) % 26) + int(sys.argv[2][3:])) % 26 + 97) if 97 <= ord(char) <= 122 else char for char in ' '.join(sys.argv[4:])]))
    else:
        lines = []
        while True:
            try:
                line = raw_input()
            except EOFError:
                break
            if line == '':
                break
            lines.append(line)
        text = '\n'.join(lines)

        if sys.argv[2] == 'rot':
            for x in range(26):
                print('ROT ' + str(x) + ': ' +''.join([chr((((ord(char) - 65) % 26) + x) % 26 + 65) if 90 >= ord(char) >= 65 else chr((((ord(char) - 97) % 26) + x) % 26 + 97) if 97 <= ord(char) <= 122 else char for char in text]))
        else:
            print(''.join([chr((((ord(char) - 65) % 26) + int(sys.argv[2][3:])) % 26 + 65) if 90 >= ord(char) >= 65 else chr((((ord(char) - 97) % 26) + int(sys.argv[2][3:])) % 26 + 97) if 97 <= ord(char) <= 122 else char for char in text]))

