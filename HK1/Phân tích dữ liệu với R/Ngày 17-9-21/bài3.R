#Bai 3: ve do thi Histograms:

library(nycflights13)
library(dplyr)
library(ggplot2)
library(tidyr)


data("weather")
weather2 <- weather %>%
  drop_na(temp)

ggplot(weather2, aes(temp)) + geom_histogram(bins=30)

