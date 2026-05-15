def count_frequency(entries):
    counts = {} # set up an empty dictionary to hold counts
    for entry in entries:
        category = entry.split(":")[0] # create sublists by splitting on ":" and selcting the first element in each list
        counts[category] = counts.get(category, 0) + 1 # accumulate counts for each category
    return counts