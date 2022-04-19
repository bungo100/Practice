def hanoi(disk, src, dest, support):
    if disk < 1:
        return

    hanoi(disk-1, src, support, dest)
    print(f'Move {disk} from {src} to {dest}')
    hanoi(disk-1, support, dest, support)

def get_move(disk, src, dest, support):
    result = []

    def _hanoi(disk, src, dest, support):
        if disk < 1:
            return

        _hanoi(disk-1, src, support, dest)
        result.append((disk, src, dest))
        _hanoi(disk-1, support, dest, src)


    _hanoi(disk, src, dest, support)
    return result






if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')
    for i in get_move(3, 'A', 'B', 'C'):
        print(i)

