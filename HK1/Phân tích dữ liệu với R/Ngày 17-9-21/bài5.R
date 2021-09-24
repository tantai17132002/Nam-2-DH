#Bai 5: ve bieu do barplot:

library(nycflights13)
library(dplyr)
library(ggplot2)


data(flights)

ggplot(flights, aes(carrier)) + geom_bar()  
