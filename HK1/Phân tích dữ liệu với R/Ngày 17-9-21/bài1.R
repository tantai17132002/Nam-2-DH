# Bài 1: Ve do thi scatter:

library(nycflights13)
library(dplyr)
library(ggplot2)
library(tidyr)

data("airlines")
data("flights")

as <- flights[flights$carrier == "AS",]
as2 <- as %>%
  na.omit()

ggplot(data = as2, aes(x = dep_delay, y = arr_delay)) + geom_point()
