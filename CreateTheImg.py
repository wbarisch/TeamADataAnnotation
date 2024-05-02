import numpy as np
import tables
import matplotlib.pyplot as plt

SIZE_X = 64*4
SIZE_Y = 64*4

nb_data = 2000

path = 'Phantom.hdf5'

data = np.zeros((nb_data, SIZE_X, SIZE_Y, 3), dtype='float32')

hdf5_file = tables.open_file(path, mode='r')

for h in range(nb_data):
    data[h] = hdf5_file.root.test[h]
hdf5_file.close()

for i in range(nb_data):
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(data[i, ..., 0], cmap='gray')
    ax.set_title('Image')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig(f'Phantom_{i}.png')
    plt.close()