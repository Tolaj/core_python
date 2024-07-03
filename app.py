    # How to import numpy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
python_list = [1,2,3,4,5]
python_list2 = [0.5,2.5,3.5,4.5,5]
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis

plt.hist(np_normal_dis, color="red", bins=21)
plt.show()