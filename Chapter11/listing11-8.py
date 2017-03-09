with open(filename) as f:
    while True:
        line = f.readline()
        if not line: break
        process(line)