'''
Dieses Skript ermöglicht das Erstellen eines Tortendiagramms zur Visualisierung des Semesterbeitrags im XKCD Style.

Usage: python3 bilder/generate_semesterbeitrag_piechart.py
Outputs: bilder/semesterbeitrag.png, bilder/semesterbeitrag_grayscale.png
'''

import matplotlib.pyplot as plt
from PIL import Image

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'VS-Beitrag', 'VRNextbike',  'Studierendenwerk', 'VRN-Semesterticket','Verwaltungskostenbeitrag'

# Values taken from https://www.stura.uni-heidelberg.de/finanzen/vs-beitrag/
sizes = [10, 2.5, 54, 35.3, 70]

explode = (0.2, 0, 0, 0, 0) # moved a bit outwards for better readability

colors = ['tab:orange', 'tab:blue', 'tab:green','tab:purple',  'tab:red']


with plt.xkcd(): # enables xkcd style

    plt.figure(figsize=(7,4))

    plt.title("Wohin fließt mein Semesterbeitag?")

    p, tx, autotexts = plt.pie(sizes, explode=explode, labels=labels, autopct='',
            shadow=True, startangle=310, colors=colors)
    
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # sets description with actual values. No decimal places if round value, otherwise two places
    for i, a in enumerate(autotexts):
        a.set_text("{:.2f} €".format(sizes[i]).replace('.00','').replace('.',','))

    plt.savefig('bilder/semesterbeitrag')

    # grayscale version for printing    
    img = Image.open('bilder/semesterbeitrag.png').convert('LA')
    img.save('bilder/semesterbeitrag_grayscale.png')