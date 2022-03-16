#!/usr/bin/ pypy

from collections import Counter 
import math

def knn(data, query, k, distance_fn, choice_fn) -> None :
    neighbor_distances_and_indices = []
    for index, example in enumerate(data) :
        # calculate distance between the 
        # query example and current example from data.
        distance = distance_fn(example[:-1], query)

        # add the distance and the index of the 
        # example to an ordered collection
        neighbor_distances_and_indices.append((distance, index))

    # sort the ordered collection of distances and indices from
    # the smallest to largest (in ascending order) by the distances
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)

    # pick the first k entries from the sorted collection
    k_nearest_distanances_and_indices = sorted_neighbor_distances_and_indices[:k]

    # get the label of selected k entries
    k_nearest_labels = [data[i][-1] for distance, i in k_nearest_distanances_and_indices]

    # if regression (choice_fn = mean), returns average of k labels
    # if classification (choice_fn = mode), return mode of the k labels
    return k_nearest_distanances_and_indices, choice_fn(k_nearest_labels)


def mean(labels) -> float :
    return sum(labels) / len(labels)

def mode(labels) -> int or float :
    return Counter(labels).most_common(1)[0][0]

def euclidean_distance(point1, point2) -> float :
    sum_squared_distance = 0
    for i in range(len(point1)) :
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def main() -> None :
    """
    Regression data
    column 0: height(inches)
    column 1: weight(pounds)
    """
    reg_data = [
       [65.75, 112.99],
       [71.52, 136.49],
       [69.40, 153.03],
       [68.22, 142.34],
       [67.79, 144.30],
       [68.70, 123.30],
       [69.80, 141.49],
       [70.01, 136.46],
       [67.90, 112.37],
       [66.49, 127.45],
    ]
    # Question:
    # Given the data we have, what's the best-guess at someone's weight if they are 60 inches tall?
    reg_query = [60]
    reg_k_neares_neighbors, reg_predict = knn(reg_data, reg_query, k = 3, 
                                            distance_fn = euclidean_distance, choice_fn = mean)

    print(f"regression outcome: {reg_predict:.2f}")
    '''
    # Classification Data
    # 
    # Column 0: age
    # Column 1: likes pineapple
    '''
    clf_data = [
       [22, 1],
       [23, 1],
       [21, 1],
       [18, 1],
       [19, 1],
       [25, 0],
       [27, 0],
       [29, 0],
       [31, 0],
       [45, 0],
    ]
    # Question:
    # Given the data we have, does a 33 year old like pineapples on their pizza?
    clf_query = [52]
    clf_k_nearest_neighbors, clf_prediction = knn(
        clf_data, clf_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )
    print(f"classification outcome: {clf_prediction}")

if __name__ == "__main__" :
    main()

# $ pypy Knn.py                 
# regression outcome: 128.25
# classification outcome: 0