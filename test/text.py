from tqdm import tqdm
import time

for i in tqdm(range(10), desc='Training Model on 10 Epochs'):
    time.sleep(0.01)
    for x in tqdm(range(10000), desc=f'Epoch {i}'):
        time.sleep(0.001)