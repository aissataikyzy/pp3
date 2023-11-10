import numpy as np
import random 
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go

x = list(np.random.randint(0, 15, 20))
y = list(np.random.randint(0, 15, 20))

letters_org = [chr(i) for i in range(ord('a'), ord('2') + 1)]
letters = letters_org[:len(y)]

df = pd.DataFrame(list(zip(x, y, letters)), columns=['x', 'y', 'point'])
df = df.append(df.iloc[0]).reset_index()

class SA:
    def __init__(self, iterations, temp, df, gamma):
        self.iterations = iterations
        self.temp = temp
        self.df = df
        self.gamma = gamma

    def total_distance(df):

        def euclidean_distance(x1, x2, y1, y2):
            return np.sqrt((x1-x2)**2+(y1-y2)**2)
        
        distance = 0 
        for idx in range(0, len(df)):
            if idx +1 >= len(df):
                break
            distance += euclidean_distance(df["x"].loc[idx], df["x"].loc[idx+1], 
                                           df["y"].loc[idx], df["y"].loc[idx+1])
        return distance
    def cooling_temp(gamma, temp):
        return gamma*temp
    
    def check_accept(temp, new_solution, current_solution):
        prob = min(1, np.exp(-(new_solution - current_solution)/temp))
        if prob > random.uniform(0, 1):
            return True
        else:
            return False
        
    def swap_elements(df):
        df_new = df.copy()
        swap_list_indx = range(1, len(df) -1)
        i = random.randint(swap_list_indx[0], swap_list_indx[-1])
        j = random.randint(swap_list_indx[0], swap_list_indx[-1])

        if i == j:
            while i == j:
                j = random.randint(swap_list_indx[0], swap_list_indx[-1])

        df_new.iloc[i], df_new.iloc[j] = df_new.iloc[j].copy(), df_new.iloc[i].copy()
        return df_new
    
    def run(self):
        temp = self.temp
        gamma = self.gamma
        df = self.df

        scores = []
        best_scores = []
        temps = []

        current = self.total_distance(self.df)
        best = self.total_distance(self.df)

        for _ in range(self.iterations):
            df_new = self.swap_elements(df)
            new = self.total_distance(df_new)
            scores.append(new)

            if new < best:
                best_df = df_new.copy()
                best = new.copy()
            best_scores.append(best)

            if self.check_accept(temp, new, current):
                df = df_new.copy()
                current = new.copy()

            temps.append(temp)
            temp = self.cooling_temp(gamma, temp)

        return scores, best_scores, temps, best_df
    
iterations = 1000
temp = 1000
gamma = 0.99

sa = SA(iterations, temp, df, gamma)
scores, best_scores, temps, best_df = sa.run()
fig = px.line(best_df, x='x', y='y', text='point', title='The best route')
fig.update_layout(template = 'simple_white', width=750, title_x=0.5, font=dict(size=18))
fig.update_trances(textposition='top center')
fig.show()
print(sa) 