
library(tidyverse)


ipod <- sample(c(rep(1, 250),
                 rep(2,300),
                 rep(3, 600),
                 rep(4, 800),
                 rep(5, 550),
                 rep(6, 350),
                 rep(7, 100),
                 rep(8, 25),
                 rep(9, 20),
                 rep(10, 5)))
ipod

# Lay ra mau co kich thuoc = 25 (bai hat)-Lap lai viec lay mau 50 lan.
# & ve bieu do tan suat cac bai hat co do dai tu 1 -> 10phut
ipod2 <- NULL
for (i in c(1:50)){
  ipod2 <- c(ipod2, sample(ipod,25))
}
ipod2

a <- data.frame(ipod2)
a 
ggplot(a, aes(x=ipod2)) + geom_histogram(binwidth = 0.5)

#xac suat xuat hien nhung bai hat co do dai 6 phut tro di
b <- table(a)
(b[6]+b[7]+b[8]+b[9]+b[10])/(50*25)

# Lay ra mau co kich thuoc = 25 (bai hat)-Lap lai viec lay mau 500 lan.
# & ve bieu do tan suat cac bai hat co do dai tu 1 -> 10phut
ipod3 <- NULL
for (i in c(1:500)){
  ipod3 <- c(ipod3, sample(ipod,25))
}
ipod3

c <- data.frame(ipod3)
c 
ggplot(c, aes(x=ipod3)) + geom_histogram(binwidth = 0.5)

#xac suat xuat hien nhung bai hat co do dai 6 phut tro di
d <- table(c)
(d[6]+d[7]+d[8]+d[9]+d[10])/(500*25)

# Lay ra mau co kich thuoc = 30 (bai hat)-Lap lai viec lay mau 30 lan.
# & ve bieu do tan suat cac bai hat co do dai tu 1 -> 10phut
ipod4 <- NULL
for (i in c(1:30)){
  ipod4 <- c(ipod4, sample(ipod,30))
}
ipod4

e <- data.frame(ipod4)
e 
ggplot(e, aes(x=ipod4)) + geom_histogram(binwidth = 0.5)

#xac suat xuat hien nhung bai hat co do dai 6 phut tro di
f <- table(e)
(f[6]+f[7]+f[8]+f[9]+f[10])/(30*30)









