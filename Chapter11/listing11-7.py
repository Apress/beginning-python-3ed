with open(filename) as f:
    while True:
        char = f.read(1)
        if not char: break
        process(char)