

if __name__ == '__main__':

    with open('sources/female-given-names.csv') as f:
        female_names = f.read().split('\n')
    with open('sources/male-given-names.csv') as m:
        male_names = m.read().split('\n')

    set_female = set(female_names)
    set_male = set(male_names)

    values = set_female.intersection(set_male)
    print(values)

