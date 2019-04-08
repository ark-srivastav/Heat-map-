import matplotlib.pyplot as plt
import matplotlib.cm
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import first
import pandas as pd
import numpy as np

import logging
logging.basicConfig(level=logging.INFO)
logging.info("Map Rendering Module")

def rendermap():
    fig, ax = plt.subplots(figsize=(10,20))
    m = Basemap(resolution='i', # c, l, i, h, f or None
            projection='merc',
            lat_0=77.95, lon_0=24.84,
            llcrnrlon=67.86, llcrnrlat= 6.5546, urcrnrlon=97.3956, urcrnrlat=37.2209)

    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
    m.readshapefile('C:/Users/hp/Desktop/proj shiz/Minor/Processed-Data/India_SHP/INDIA','INDIA')
    m.drawcoastlines()
    yearly_rainfall=[]
    logging.info("Yearly Average Recieved ... Joining with shp file ")
    for state_info in m.INDIA_info:
        state=state_info['ST_NAME'].upper()
        rainfall=0.0
        #print(state)
        for x in first.x:
            #print(x[0])
            if x[0].strip() == state.strip():
                rainfall=x[1]
                #print(rainfall)
                break
        yearly_rainfall.append(rainfall)
    
    df_poly = pd.DataFrame({
        'shapes': [Polygon(np.array(shape), True) for shape in m.INDIA],
        'area': [area['ST_NAME'] for area in m.INDIA_info],
        'yearly_rainfall' : yearly_rainfall
    })
    #print(df_poly)





    shapes = [Polygon(np.array(shape), True) for shape in m.INDIA]
    # Create a colormap
    cmap = plt.get_cmap('Oranges')   
    # Create a patch collection. Create patches on the top of the map, not beneath it (zorder=2)
    pc = PatchCollection(shapes, zorder=2)

    norm = Normalize()
    # Set color according to the Yearly Rainfall of the state
    pc.set_facecolor(cmap(norm(df_poly['yearly_rainfall'].fillna(0).values)))
    ax.add_collection(pc)

    # Create a mapper to map color intensities to values
    mapper = matplotlib.cm.ScalarMappable(cmap=cmap)
    mapper.set_array(yearly_rainfall)
    plt.colorbar(mapper, shrink=0.8,label=r'centimeters')  
    # Set title for the plot
    ax.set_title("Yearly Rainfall OF INDIAN STATES :)")
    # Change plot size and font size
    plt.rcParams['figure.figsize'] = (30,30)
    plt.rcParams.update({'font.size': 20})
    plt.show()



#print(first.x)
rendermap()
#  westlimit=67.86; southlimit=6.5546; eastlimit=97.3956; northlimit=37.2209
""" [[[66.765425697,7.3796296039],[98.3364370625,7.3796296039],[98.3364370625,37.242511255],[66.765425697,37.242511255],[66.765425697,7.3796296039]]]"""