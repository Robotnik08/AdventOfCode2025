import z3

input = open("input.txt").read().strip()
lines = input.split("\n")

buttons = []
joltages = []

for line in lines:
    parts = line.split(" ")
    
    parts.pop(0)

    joltages.append(tuple(map(int, parts.pop()[1:-1].split(","))))

    buttons_tuples = []
    for part in parts:
        button = tuple(map(int, part[1:-1].split(",")))
        buttons_tuples.append(button)

    buttons.append(buttons_tuples)

total = 0

for i in range(len(buttons)):

    button_count = len(buttons[i])
    counter_count = len(joltages[i])

    x = [z3.Int(f"x{i}") for i in range(button_count)]
    solver = z3.Optimize()

    for xi in x:
        solver.add(xi >= 0)

    for c in range(counter_count):
        terms = [x[j] for j in range(button_count) if c in buttons[i][j]]
        if not terms:
            if joltages[i][c] != 0:
                print("Something is wrong")
                exit()
            else:
                solver.add(z3.IntVal(0) == joltages[i][c])
        else:
            solver.add(z3.Sum(terms) == joltages[i][c])

    solver.minimize(z3.Sum(x))

    if solver.check() != z3.sat:
        print("Something is wrong")
        exit()

    model = solver.model()
    
    total += sum(model[i].as_long() for i in x)

print("Part 2:", total)