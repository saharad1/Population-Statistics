import pandas
import math


# The function reads the data from the csv file and filter the unnecessary features, then returns the dictionary.
def load_data(path, features):
    df = pandas.read_csv(path)
    data = df.to_dict(orient="list")

    out = []
    for key in data.keys():
        if key not in features:
            out.append(key)
    for item in out:
        del data[item]
    for index, element in enumerate(data['earnings']):
        data['earnings'][index] = math.log10(element)
    return data


# The function returns 2 different dictionaries based on the feature and its sub-values given in a set.
def filter_by_features(data, feature, values):
    new_dict = {x: [] for x in data.keys()}
    new_dict2 = {x: [] for x in data.keys()}
    for index, element in enumerate(data[feature]):
        if element not in values:
            for keys in data.keys():
                new_dict[keys].append(data[keys][index])
        else:
            for keys in data.keys():
                new_dict2[keys].append(data[keys][index])
    return new_dict2, new_dict


# The function prints the statistics data of the required features.
def print_details(population, data, features, statistic_functions):
    print(population + ":")
    for keys in features:
        print(keys.capitalize() + ":", end=" ")
        for func in statistic_functions:
            if func == statistic_functions[len(statistic_functions) - 1]:
                print(func(list(data[keys])), end=" ")
            else:
                print(func(list(data[keys])), end=", ")
        print("")
