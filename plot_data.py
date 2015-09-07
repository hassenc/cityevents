import pandas as pd
import numpy as np
import locale
locale.setlocale(locale.LC_NUMERIC, '')

all = pd.read_json("allData.json")
all.TicketPrice = all.TicketPrice.apply(lambda x: "$0.00" if isinstance(x, basestring) and x == "" else x)
all['price'] = all.TicketPrice.map(lambda x : float(locale.atof(x[1:])))
all['isFree'] = all.price.apply(lambda x: 1 if x == 0 else 0)
all['city'] = all.RegionId.map({3639:'Los Angeles',3633:'New York'})

#all.price.argmax()
all = all.drop(all.index[52])

gro = all.groupby(['CategoryName','city'])
temp0 = gro.CategoryName.count()
my_plot1 = temp0.unstack().plot(kind='bar',title="Number of events per event category [January 2015 - December 2015]",figsize=(10, 6))
my_plot1.set_xlabel("Event category")
my_plot1.set_ylabel("Number of events")


temp2 = gro.isFree.sum()/gro.isFree.count()
my_plot2 = temp2.unstack().plot(kind='bar',title='Percentage of Free events [January 2015 - December 2015]',figsize=(10, 6))
my_plot2.set_xlabel("Event category")
my_plot2.set_ylabel("Percentage of Free events")

temp1 = gro.price.sum()/(gro.price.count()-gro.isFree.sum())
my_plot3 = temp1.unstack().plot(kind='bar',title='Mean price per event category [January 2015 - December 2015]',figsize=(10, 6))
my_plot3.set_xlabel("Event category")
my_plot3.set_ylabel("Mean price of events")
