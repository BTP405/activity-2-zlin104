def report(func):
    def inner(arg):
        lines = func(arg)
        for index, line in enumerate(lines):
            print('Numbers read: ', line)
            print('Count of numbers read: ', len(line))
            avg = sum(line) / len(line) if len(line) > 0 else 0
            print('Average: ', avg)
            print('Max: ', max(line) if len(line) > 0 else 'No numbers' )            
    return inner

@report
def printStats(t):
    f = open(t, 'r')
    lines = []
    for line in f:
        line = [int(num) for num in line.split()]
        lines.append(line)
    return lines

printStats('a.txt')
