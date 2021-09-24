#Bai 2: ve do thi Linegraphs:

library(nycflights13)
library(dplyr)
library(ggplot2)


data("weather")

ewr <- subset(weather,weather$origin == "EWR"&
                weather$month == "1"&weather$day<=15)

ggplot(ewr, aes(x=time_hour, y=temp)) + geom_line()

                