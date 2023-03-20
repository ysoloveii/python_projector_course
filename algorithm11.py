def get_cats_with_hats():

    # set by default that all cats doesn't have hats
    array_of_cats = [False] * (100 + 1)

    cats_with_hats_on = []

    # walking around 100 times
    for num in range(1, 100 + 1):
        # each time we visit 100 cats
        for cat in range(1, 100 + 1):
            # determine whether to visit the cat
            if cat % num == 0:
                # remove or add hat depending on
                # whether the cat already has one
                if array_of_cats[cat] is True:
                    array_of_cats[cat] = False
                else:
                    array_of_cats[cat] = True

    # add all number of each cat with a hat to list
    for cat in range(1, 100 + 1):
        if array_of_cats[cat] is True:
            cats_with_hats_on.append(cat)

    return cats_with_hats_on


print('Cats that have hats: ' + str(get_cats_with_hats())[1:-1])
