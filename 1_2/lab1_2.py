class Vector:

    def __init__(self, components):
        self.components = components

    def __str__(self):
        return " ".join(str(x) for x in self.components)

    def dimension(self):
        return len(self.components)

    def length(self):
        return sum(x ** 2 for x in self.components) ** 0.5

    def mean(self):
        return sum(self.components) / len(self.components)

    def max_component(self):
        return max(self.components)

    def min_component(self):
        return min(self.components)


def read_vectors_from_file(filename):
    vectors = []
    with open(filename, 'r') as file:
        for line in file:
            components = [float(x) for x in line.strip().split()]
            vectors.append(Vector(components))
    return vectors


def find_vector_with_max_dimension_and_min_length(vectors):
    max_dimension_vector = min_length_vector = None
    max_dimension = -1 # найменше можливе ціле значення
    min_length = float('inf') # додатна нескінченність

    for vector in vectors:
        dimension = vector.dimension()
        if dimension > max_dimension:
            max_dimension = dimension
            max_dimension_vector = vector
            min_length = vector.length()
        elif dimension == max_dimension and vector.length() < min_length:
            min_length = vector.length()
            min_length_vector = vector

    return max_dimension_vector if min_length_vector is None\
        else min_length_vector


def find_vector_with_max_length_and_min_dimension(vectors):
    max_length_vector = min_dimension_vector = None
    max_length = -1
    min_dimension = float('inf')

    for vector in vectors:
        length = vector.length()
        if length > max_length:
            max_length = length
            max_length_vector = vector
            min_dimension = vector.dimension()
        elif length == max_length and vector.dimension() < min_dimension:
            min_dimension = vector.dimension()
            min_dimension_vector = vector

    return max_length_vector if min_dimension_vector is None\
        else min_dimension_vector


def average_length(vectors):
    total_length = sum(vector.length() for vector in vectors)
    return total_length / len(vectors)


def count_vectors_above_average_length(vectors):
    avg_len = average_length(vectors)
    count = sum(1 for vector in vectors if vector.length() > avg_len)
    return count


def vector_with_max_max_component(vectors):
    max_max_component_vector = None
    max_component = -float('inf') # від'ємна нескінченність

    for vector in vectors:
        current_max_component = vector.max_component()
        if current_max_component > max_component:
            max_component = current_max_component
            max_max_component_vector = vector
        elif current_max_component == max_component:
            min_min_component_of_existing = min(max_max_component_vector.min_component(), vector.min_component())
            if min_min_component_of_existing == vector.min_component():
                max_max_component_vector = vector

    return max_max_component_vector


def vector_with_min_min_component(vectors):
    min_min_component_vector = None
    min_component = float('inf')

    for vector in vectors:
        current_min_component = vector.min_component()
        if current_min_component < min_component:
            min_component = current_min_component
            min_min_component_vector = vector
        elif current_min_component == min_component:
            max_max_component_of_existing = max(min_min_component_vector.max_component(), vector.max_component())
            if max_max_component_of_existing == vector.max_component():
                min_min_component_vector = vector

    return min_min_component_vector


files = ["input01_2.txt", "input02_2.txt", "input03_2.txt", "input04_2.txt"]


for file in files:
    print(f"результати для {file}:")
    vectors = read_vectors_from_file(file)

    vector_max_dim_min_len = find_vector_with_max_dimension_and_min_length(vectors)
    print(f"вектор з найбільш розмірністю та найменш довжиною: {vector_max_dim_min_len}")

    vector_max_len_min_dim = find_vector_with_max_length_and_min_dimension(vectors)
    print(f"вектор з найбільш довжиною та найменш розмірністю: {vector_max_len_min_dim}")

    avg_len = average_length(vectors)
    print(f"середня довжина вектора: {avg_len}")

    count_above_avg_len = count_vectors_above_average_length(vectors)
    print(f"к-сть векторів з довжиною більше за середню: {count_above_avg_len}")

    max_max_comp_vector = vector_with_max_max_component(vectors)
    print(f"вектор з макс найбільшою компонентою: {max_max_comp_vector}")

    min_min_comp_vector = vector_with_min_min_component(vectors)
    print(f"вектор з мін найменшою компонентою: {min_min_comp_vector}")

    print()