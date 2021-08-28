

if __name__ == '__main__':

    with open('../names/french/sources/female-given-names.csv') as f:
        female_names = f.read().split('\n')
    with open('../names/french/sources/male-given-names.csv') as m:
        male_names = m.read().split('\n')

    set_female = set(female_names)
    set_male = set(male_names)

    values = set_female.intersection(set_male)
    print(values)
    with open('unisex-names.csv', 'w') as fp:
        for value in values:
            fp.write(value + '\n')

