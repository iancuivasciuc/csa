import sys
import random


def generate(input_file):
    fin = open(input_file, 'w')
    files = set()

    seed = random.randrange(sys.maxsize)
    rng = random.Random(seed)

    num_commands = 40
    fin.write(f"{num_commands}\n")

    for _ in range(num_commands):
        command = random.randint(1, 4)
        fin.write(f"{command}\n")

        if command == 1:
            num_adds = random.randint(1, 10)
            fin.write(f"{num_adds}\n")

            for _ in range(num_adds):
                fd = random.randint(1, 255)
                while fd in files:
                    fd = random.randint(1, 255)
                fin.write(f"{fd}\n")
                files.add(fd)

                dim = random.randint(9, 9000)
                fin.write(f"{dim}\n")
        elif command == 2:
            fd = random.choice(list(files))
            fin.write(f"{fd}\n")
        elif command == 3:
            fd = random.choice(list(files))
            files.remove(fd)
            fin.write(f"{fd}\n")
        elif command == 4:
            pass

    fin = fin.close()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 generator.py <input.txt>")
        return

    input_file = sys.argv[1]
    generate(input_file)


if __name__ == '__main__':
    main()
