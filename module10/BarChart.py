# This program is a simple example utilizing the ggplot module to create an example bar chart
# Joshua Snyder - 03/28/2020


from ggplot import *

ggplot(aes(x='factor(cyl)', fill='factor(cyl)'), data=mtcars) + \
    geom_bar()