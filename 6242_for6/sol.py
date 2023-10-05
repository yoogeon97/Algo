def count_blood(blood):
    new = {}
    for i in blood:
        new[i] = new.get(i, 0) +1
    return new

print(count_blood(['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']))