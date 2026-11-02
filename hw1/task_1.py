def main():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print('есть в обоих городах:', moscow & kazan)
    print('только в москве:', moscow - kazan)
    print('только в казани:', kazan - moscow)
    print('всего разных товаров:', len(moscow | kazan))


if __name__ == '__main__':
    main()
