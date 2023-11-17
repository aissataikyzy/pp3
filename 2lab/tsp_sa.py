import math
import random

class SimulatedAnnealing(object):
    def __init__(self, coords, temp, stop_temp):        
        self.optimum = 9352
        
        self.coords = coords
        self.N = len(coords)
        
        self.neighbor_count = 0
        self.max_neighbors = (self.N - 3) * self.N // 2
        
        self.T = temp
        self.T_decrease = 0.99
        self.stop = stop_temp
        self.T_const = self.T
        
        self.costs = []
        self.best_cost = float("inf")
        self.ct = [i for i in range(self.N)]
        self.best_solution = None
        
        self.iteration = 1

    def distance(self, m, n):
        x, y = self.coords[m], self.coords[n]
        dx = x[0] - y[0]
        dy = x[1] - y[1]
        dist = math.sqrt(dx**2 + dy**2)
        return dist

    def calculate_fitness(self, solution):
        current_cost = 0
        for i in range(self.N):
            current_cost += self.distance(solution[i % self.N], solution[(i + 1) % self.N])
        return current_cost

    def generate_random_path(self, N):
        path = list(range(self.N))
        random.shuffle(path)
        return path

    def initial_solution(self):
        solution = self.generate_random_path(self.N)
        current_cost = self.calculate_fitness(solution)

        if current_cost < self.best_cost:
            self.best_cost = current_cost
            self.best_solution = solution

        self.costs.append(current_cost)
        return solution, current_cost

    def prob(self, candidate_cost):
        delta = candidate_cost - self.current_cost
        return math.exp(-delta/self.T), delta

    def transfer(self, candidate):
        candidate_cost = self.calculate_fitness(candidate)
        if candidate_cost <= self.current_cost:
            self.current_cost = candidate_cost
            self.current_solution = candidate
            if candidate_cost < self.best_cost:
                self.best_cost = candidate_cost
                self.best_solution = candidate
        else:
            f, delta = self.prob(candidate_cost)
            
            if delta < 0 or random.random() < f:
                self.current_cost = candidate_cost
                self.current_solution = candidate
                
        self.neighbor_count += 1

        if self.neighbor_count >= self.max_neighbors:
            self.T *= self.T_decrease
            self.neighbor_count = 0


    def SA(self):
        self.current_solution, self.current_cost = self.initial_solution()

        while self.T > self.stop: #and self.iteration < self.stop_iter:
            candidate = list(self.current_solution)
            q = random.randint(2, self.N - 1)
            w = random.randint(0, self.N - 1)
            candidate[w:(w + q)] = reversed(candidate[w:(w + q)])

            self.transfer(candidate)

            with open('qatar.txt', 'a') as file:
                            file.write(f"Iteration: {self.iteration}\n")
                            file.write(f"Temperature: {self.T}\n")
                            file.write(f"Current cost: {self.current_cost}\n")
                            file.write(f"Current solution: {self.current_solution}\n")
                            
            self.iteration += 1
                
            self.costs.append(self.current_cost)

            with open('costs.txt', 'a') as p:
                p.write(str(self.current_cost) + "\n")
        
        print('Best cost:', self.best_cost)
        with open('qatar.txt', 'a') as file:
            file.write(f"Best cost: {self.best_cost}\n")
            file.write(f"Best route: {self.best_solution}\n")

            # file.write(f"Best solution: {solution[-1]}\n")
            proc = ((self.best_cost - self.optimum)/self.optimum)*100
            print('From known optimum:', proc)
            file.write(f"From known optimum: {proc} %\n")
    