import numpy as np

# Чтение координат городов из текстового файла
def read_city_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Разбиваем строки на координаты и парсим их
    coordinates = [line.strip().split() for line in lines]
    cities = np.array([[float(coord[0]), float(coord[1])] for coord in coordinates])

    return cities

# Расчет расстояния между двумя городами
def distance(city1, city2):
    return np.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Расчет общего расстояния маршрута
def total_distance(route, cities):
    total = 0
    for i in range(len(route) - 1):
        total += distance(cities[route[i]], cities[route[i + 1]])
    return total + distance(cities[route[-1]], cities[route[0]])

# Имитация отжига
def simulated_annealing(route, cities, initial_temperature, cooling_rate, min_probability):
    current_route = route
    current_cost = total_distance(current_route, cities)
    best_route = current_route
    best_cost = current_cost
    temperature = initial_temperature
    iteration = 0

    while temperature >= min_probability:
        new_route = current_route.copy()
        i, j = np.random.choice(len(cities), size=2, replace=False)
        new_route[i], new_route[j] = new_route[j], new_route[i]
        new_cost = total_distance(new_route, cities)
        cost_difference = new_cost - current_cost

        if cost_difference < 0 or np.random.rand() < np.exp(-cost_difference / temperature):
            current_route = new_route
            current_cost = new_cost

            if current_cost < best_cost:
                best_route = current_route
                best_cost = current_cost

        temperature *= cooling_rate
        iteration += 1

    return best_route, best_cost, iteration

# Параметры имитации отжига
initial_temperature = 1000
cooling_rate = 0.9995
min_probability = 0.001

# Указание пути к текстовому файлу с координатами городов
filename = 'qatar.txt'

# Получение координат городов из файла
cities = read_city_coordinates(filename)

# Начальное решение (порядок посещения городов)
initial_route = np.arange(len(cities))
np.random.shuffle(initial_route)

# Запуск имитации отжига
best_route, best_cost, iterations = simulated_annealing(initial_route, cities, initial_temperature, cooling_rate, min_probability)

probability_of_optimal_solution = (1 - min_probability) ** iterations

print("Лучший маршрут:", best_route)
print("Лучшее расстояние (стоимость):", best_cost)
print(iterations)
print(f"Вероятность оптимального решения: {(best_cost-9352)/9352*100:.2f}%")