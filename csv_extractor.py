import pandas as pd

keeper_sched = pd.read_csv('/home/ric/Documents/2022_Schedule_Grid.csv')

keeper_sched.rename(columns = {'Week 1': 'First', 'Week 18': 'Last'}, inplace = True)

print(keeper_sched)


