def towerOfHanoi(n, start, end, extra):
    if n == 1:
        print(f"Move disk 1 from source {start} to destination {end}")
        return
    towerOfHanoi(n-1, start, extra, end)
    print(f"move disk {n} from source {start} to destination {end}")
    towerOfHanoi(n-1, extra, end, start)


n = 3
towerOfHanoi(n, 'A', 'C', 'B')
