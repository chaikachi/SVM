import argparse

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('textfile', type = str)
    parser.add_argument('binaryfile', type = str)
    parser.add_argument('--test', action='store_true')
    return parser.parse_args()

def assemble(args):
    commands = []
    with open(args.textfile, "r") as r:
        for line in r:
            c_line = line.strip().replace(" ","")
            if c_line == "":
                continue
            f_line = c_line.split("=")
            left = f_line[0]
            right = f_line[1]
            if "-" in right:
                a = 12
                c_right = right.split("-")
                d = int(left.lstrip("*"))
                c = int(c_right[0].lstrip("*"))
                b = int(c_right[1].lstrip("*"))
                commands.append({'A': a, 'B': b, 'C': c, 'D': d})
            elif "+" in right:
                a = 7
                c_right = right.split("+")
                b = int(left.lstrip("*"))
                c = int(c_right[1].rstrip(")"))
                d = int(c_right[0].lstrip("*("))
                commands.append({'A': a, 'B': b, 'C': c, 'D': d})
            elif "*" in right:
                a = 5
                c = int(left.lstrip("*"))
                b = int(right.lstrip("*"))
                commands.append({'A': a, 'B': b, 'C': c})
            else:
                a = 13
                b = int(left.lstrip("*"))
                c = int(right)
                commands.append({'A': a, 'B': b, 'C': c})
    return commands

def test_mode(command_list):
    for line in command_list:
        parts = []
        for key, value in line.items():
            parts.append(f"{key} = {value}")
        print(", ".join(parts))

def start():
    args = parser()
    command_list = assemble(args)
    if args.test:
        test_mode(command_list)

if __name__ == "__main__":
    start()
