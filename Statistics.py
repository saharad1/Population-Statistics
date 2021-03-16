from Data import filter_by_features, print_details


def sum_list(values):
    final_sum = 0
    for x in values:
        final_sum += x
    return final_sum


def mean(values):
    final_mean = float(sum_list(values)) / len(values)
    return final_mean


def median(list_of_values):
    sorted_list = sorted(list_of_values)
    center_index = int(len(list_of_values) / 2)

    if len(list_of_values) % 2 == 0:
        result = (sorted_list[center_index] + sorted_list[center_index - 1]) / 2
    else:
        result = sorted_list[center_index]
    return result


# The function uses the filter and print details functions in order to print the calculations for relevant features.
def population_statistics(population, data, feature1, feature2, min_val, max_val, statistic_functions):
    filtered_f1, rest_filtered_f1 = filter_by_features(data, feature1, range(min_val, max_val + 1))
    print_details(population, filtered_f1, [feature2], statistic_functions)
