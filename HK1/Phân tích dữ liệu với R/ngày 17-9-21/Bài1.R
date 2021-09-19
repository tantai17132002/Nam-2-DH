# Bài 1: Ve do thi scatter:

library(nycflights13)
library(dplyr)
library(ggplot2)


data("airlines")
data("flights")

AS <- flights[flights$carrier == "AS",]
head(AS)

ggplot(data = AS, aes(x = dep_delay, y = arr_delay)) + geom_point()
