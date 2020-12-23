import numpy as np
import matplotlib.pyplot as plt
import requests
from io import BytesIO
labels = ['Josh', 'Dion', 'Christian']
colors = ['crimson', 'seagreen', 'dodgerblue']
values = [326,114,233]
height = .8
plt.barh(y=labels, width=values, height=height, color=colors, align='center')
plt.title('Who is the most popular host?', fontdict=None, loc='center', pad=None)
for i, (label, value) in enumerate(zip(labels, values)):
 response = requests.get(f'https://welcometopatchwork.com.au/wp-content/uploads/2020/05/{label}.png')
 img = plt.imread(BytesIO(response.content)) 
 plt.imshow(img, extent=[value - 70, value - 2, i - height / 2, i + height / 2], aspect='auto',zorder=2)
 
plt.xlabel('mentions')
plt.xlim(0,400)
plt.ylim(-0.5,2.5)
plt.tight_layout()
plt.savefig('popular.png', dpi=100)
plt.show()