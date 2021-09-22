
library(ISwR)

#9.1 thong ke mo ta (descriptive statistics, summary) 

setwd("E:\\Document\\Nam 2\\PTDL VS R\\Documents\\R-book-master")

igfdata <- read.table("igf.txt", header =TRUE, na.strings =".")
attach(igfdata)

names(igfdata)
igfdata

##VD 9:

mean(age) #Gia tri trung binh cua do tuoi

var(age) #Phuong sai cua tuoi

sd(age) #Doc lenh chuan cua tuoi

summary(age) #Tat ca thong tin ve 1 bien so

##Phan tich

desc <- function(x)
{
  av <- mean(x)
  sd <- sd(x)
  se <- sd/sqrt(length(x))
  c(MEAN=av, SD=sd, SE=se)
}

desc(als)

summary(igfdata)

by(igfdata, sex, summary)

##Ve bieu do

op <- par(mfrow=c(2,3)) 

hist(igfi)

hist(igfbp3) 

hist(als) 

hist(pinp) 

hist(ictp) 

hist(p3np)

#9.2 Thong ke mo ta theo tung nhom

tapply(igfi, list(sex), mean)

tapply(igfi, list(ethnicity, sex), mean)

#9.3.1 Kiem dinh t mot mau

## VD 10:

qt(0.95, 100)

t.test(age, mu=30)

#9.3.2 Kiem dinh t hai mau

t.test(igfi ~ sex)

t.test(igfi ~ sex, var.equal=TRUE)

#9.4 Kiem dinh Wilcoxon cho 2 mau (wilcox.test)

shapiro.test(igfi)

wilcox.test(igfi ~ sex)

#9.5 kiem dinh t cho cac bien so theo cap (paired t-test, t.test)

## VD 12:

## Nhap du kien

before <- c(180, 140, 160, 160, 220, 185, 145, 160, 160, 170)
after  <- c(170, 145, 145, 125, 205, 185, 150, 150, 145, 155)
bp <- data.frame(before, after)

## kiem dinh t

t.test(before, after, paired = TRUE)

t.test(before, after)

#9.6 kiem dinh Wilcoxon cho cac bien so theo cap (wilox.test)

wilcox.test(before, after, paired = TRUE)

#9.7 tan so (frequency)

table(sex)

table(ethnicity)

table(sex, ethnicity)

freq <- table(sex, ethnicity) # tao ra 1 object ten la freq de chua ket qua tan so
freq

margin.table(freq, 1) #dung ham margin.table de xem ket qua

margin.table(freq, 2)

prop.table(freq, 1) # tinh phan tram bang ham prop.table

prop.table(freq, 2)

freq/sum(freq) # tinh % cho toan bo bang

#9.8 kiem dinh ti le (proportion test, prop.test, binom.test)

##VD 13:

prop.test(69, 100, 0.50)

binom.test(69, 100, 0.50)

#9.9 so sanh ti le (prop.test, binom.test)

## VD 14:

fracture <- c(7, 20)
total <- c(100, 110)
prop.test(fracture, total)

#9.10 so sanh ti le (prop.test, chisq.test)

table(sex, ethnicity)

female <- c(4, 43, 22, 0)
total <- c(8, 60, 30, 2)
prop.test(female, total)

#9.10.1 kiem dinh Chi binh phuong (Chi squared test, chisq.test)

chisq.test(sex, ethnicity)

#9.10.2 kiem dinh Fisher(Fisher's exact test, fisher.test)

fisher.test(sex, ethnicity)





















