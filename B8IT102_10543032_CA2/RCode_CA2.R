#working directory
setwd('R:/10543032_CA2')

#get the data
commits <- read.csv('commits.csv')

#check the dataframe
class(commits)
#examining all the dataframe
head(commits)
summary(commits)

#examining the number of lines ammended
mean(commits$number)
median(commits$number)
range(commits$number)

#unique values
unique_vals <- lapply(commits, unique)
print(unique_vals)

#checking the number of unique names 
unique_vals(commits$name)

# hist examining the number of lines ammended
hist(commits$number, col = 2, main="Number of Comment Lines for Each Commit", xlab = "Number of Comment Lines Per Commit", ylab = "Total Comment Lines")

#examining string data in the set 
str(commits)
str(commits$day)
str(commits$name)

#installing necessary package for the graphs
if (!require("ggplot2")) install.packages("ggplot2") #click Run
library(ggplot2) #click Run

# graph examining the weekday of ammended code
dim(commits$day)
names(commits$day)
head(commits$day)
tail(commits$day)
summary(commits$day)

ggplot(data.frame(commits), aes(x=day), main="Histogram for Days of the Week", xlab = "Days of the week", ylab = "Number of Comment Lines") + geom_bar()

# graph examining the developer
dim(commits$name)
names(commits$name)
head(commits$name)
tail(commits$name)
summary(commits$name)

ggplot(data.frame(commits), aes(x=name), c = 2, main="Number of Comment Lines for Each Developer", xlab = "Name of Developers", ylab = "Number of Comment Lines") + geom_bar()


# graph examining the number of lines
dim(commits$number)
names(commits$number)
head(commits$number)
tail(commits$number)
summary(commits$number)

ggplot(data.frame(commits), aes(x=number), c = 2, main="Number of Comment Lines for Each Developer", xlab = "Name of Developers", ylab = "Number of Comment Lines") + geom_bar()


# table examining the number of lines ammended
table(commits$number)

# table examining the weekday of ammended code
table(commits$day)

# table examining the developer
table(commits$name)

#installing necessary package
if (!require("MASS")) install.packages("MASS") #click Run
library(MASS) #click Run

#running Chi-square to examine the relationship between the developer and the day of the week.
tbl = table(commits$name, commits$day) 
chis.test(tbl)
summary(tbl)
# showing the tableq
tbl


##Piechart
head(commits)

#piechart of day
ggplot(commits, aes(x=factor(5), fill=day))+
  geom_bar(width = 1)+
  coord_polar("y")

ggplot(commits, aes(x=day, fill=day))+
  geom_bar(width = 1)+
  coord_polar("y")

#piechart of developers
ggplot(commits, aes(x=factor(2), fill=name))+
  geom_bar(width = 1)+
  coord_polar("y")

ggplot(commits, aes(x=name, fill=day))+
  geom_bar(width = 1)+
  coord_polar("y")

#examine the relationship between the DAYS and lines of code
levels(commits$day)

commits$group <- ordered(commits$day, levels =  c("Friday", "Monday", "Thursday", "Tuesday", "Wednesday"))

#installing necessary package
if (!require("dplyr")) install.packages("dplyr") #click Run
library(dplyr) #click Run

group_by(commits, day) %>%
  summarise(
    count = n(),
    mean = mean(number, na.rm = TRUE),
    sd = sd(number, na.rm = TRUE)
  )



# Compute the analysis of variance
res.aov <- aov(number ~ day, data = commits)

# Summary of the analysis
summary(res.aov)

#no need for TukeyHSD(res.aov) because it is not significant
TukeyHSD(res.aov)

#examine the relationship between the names and lines of code
levels(commits$name)

group_by(commits, name) %>%
  summarise(
    count = n(),
    mean = mean(number, na.rm = TRUE),
    sd = sd(number, na.rm = TRUE)
  )

#examine the relationship between the DAYS and lines of code
levels(commits$name)


# Compute the analysis of variance
res.aov1 <- aov(number ~ name, data = commits)

# Summary of the analysis
summary(res.aov1)

TukeyHSD(res.aov1)

# Homogeneity of variances
plot(res.aov, 1) #violates the assumumption of normality
plot(res.aov1, 1) #violates the assumumption of normality


if (!require("car")) install.packages("car") #click Run
library(car)

# homogeneity of variances
leveneTest(number ~ day, data = commits) #p = 0.2085 doesn't violate the assumumption of normality
leveneTest(number ~ name, data = commits) # p =  0.001 violates the assumumption of normality
# if p-value is not less the significance level of 0.05, 
#there is no evidence to suggest that the variance across groups is statistically significantly different.


# 2. Normality
plot(res.aov, 2) #violates the assumumption of normality
plot(res.aov1, 2) #violates the assumumption of normality


# Kruskal-Wallis rank sum test
day.krus <- kruskal.test(number ~ day, data = commits)
print(day.krus)


name.krus <- kruskal.test(number ~ name, data = commits)
print(name.krus)

#upload a package
if(!require(devtools)) install.packages("devtools")
devtools::install_github("kassambara/ggpubr")

library("ggpubr")
#boxplot - does not look great
ggboxplot(commits, x = "day", y = "number", 
          main="Number of Comment Lines for Each Day",
          color = "day", palette = c("#00AFBB", "#E7B800", "#FC4E07",  "#00AFBB", "#E7B800"),
          order = c("Fri", "Mon", "Thu", "Tue", "Wed"),
          ylab = "Number of Lines", xlab = "Weekday")

