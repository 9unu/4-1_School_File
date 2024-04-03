newdata <- read.csv("matched_data_lalonde_revised.csv")

mynewmodel <- lm(revenue ~ treat + after + treat:after, data = newdata)

summary(mynewmodel)

