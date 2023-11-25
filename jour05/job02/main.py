def draw_rectangle(width, height):
    if width < 2 or height < 2:
        return

    print('|' + '-' * (width - 2) + '|')

    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    print('|' + '-' * (width - 2) + '|')

draw_rectangle(10, 3)
