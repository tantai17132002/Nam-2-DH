#Bai 4: ve bieu do boxplot:

library(nycflights13)
library(dplyr)
library(ggplot2)
library(tidyr)


data(weather)
weather2 <- weather %>%
  drop_na(temp)
  
ggplot(weather2, aes(x=factor(month), y=temp)) + geom_boxplot()
