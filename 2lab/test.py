from tsp_sa import SimulatedAnnealing

T = 70
stop_T = 3

if __name__ == "__main__":
    cities = []
    coords = []

    with open('qatar.txt') as data:
        c = data.read().split('\n')
        [cities.append(i) for i in c]

        for i in cities:
            x, y, z = i.split()
            cord = [float(y), float(z)]
            coords.append(cord)

    sa = SimulatedAnnealing(coords, T, stop_T)
    sa.SA()
