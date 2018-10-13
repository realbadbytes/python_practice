import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

r = requests.get('https://seclists.org/bugtraq')
html = r.text
parsed_html = BeautifulSoup(html, features='html.parser')
# <table class="calendar">
tables = parsed_html.findAll('table')
calendar = tables[len(tables)-1]
print calendar.prettify()
counts = calendar.findAll('a')
# Y
volume = list()
for c in counts:
    volume.append(int(c.string))
print volume
# X
indices = range(len(volume))
print indices
# graph the fucking shit
import numpy as np
from scipy.interpolate import interp1d
plt.xlabel("1993 through 2018")
plt.ylabel("bugtraq message count")
volume = np.array(volume)
indices = np.array(indices)
x_new = np.linspace(indices.min(), indices.max(), 1000)
f = interp1d(indices, volume, kind='cubic')
y_smooth = f(x_new)
#plt.scatter(indices, volume, 10)
plt.plot(x_new, y_smooth)
#plt.scatter(indices, volume)
plt.show()

