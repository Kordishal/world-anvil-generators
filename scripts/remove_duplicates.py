

if __name__ == '__main__':

    with open('duplicated_list.txt') as f:
        names = f.read().split('\n')

    names = sorted(set(names), key=lambda x: x.lower())

    with open('unique_names.txt', 'w') as f:
        for name in names:
            f.write(name + '\n')
