import sys
from Data import load_data, print_details, filter_by_features
from Statistics import sum_list, median, mean, population_statistics


def main(argv):
    print("Question1:")
    stat_function = [sum_list, mean, median]
    population_name = ["Men", "Women", "All"]
    data = load_data(argv[1], argv[2])
    dict_women, dict_men = filter_by_features(data, 'female', {1})
    dict_list = [dict_men, dict_women, data]
    for i in range(3):
        print_details(population_name[i], dict_list[i], ['age', 'earnings', 'hours', 'week'], stat_function)
    # Here is the end of question 1
    print("Question2:")
    married, not_married = filter_by_features(dict_women, 'marital', {1, 2, 3})
    print("If 0<=Y<=10, then:")
    population_statistics("Married Women", married, 'education', 'earnings', 0, 10, stat_function[1:3])
    population_statistics("Unmarried Women", not_married, 'education', 'earnings', 0, 10, stat_function[1:3])
    print("If 11<=Y<=20, then:")
    population_statistics("Married Women", married, 'education', 'earnings', 11, 20, stat_function[1:3])
    population_statistics("Unmarried Women", not_married, 'education', 'earnings', 11, 20, stat_function[1:3])
    # The end of question 2


if __name__ == '__main__':
    main(sys.argv)
