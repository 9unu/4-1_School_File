#(p.34)
#데이터 활용 패키지 및 시각화 패키지 설치 및 불러오기
install.packages("dplyr")
install.packages("ggplot2")
library(dplyr)
library(ggplot2)

#데이터 불러오기
mydata <- read.csv("BEDA_4_RDD_data_carpenterdobkin.csv", sep=',')

#데이터 둘러보기
head(mydata)
summary(mydata)

#시각화 기본
mydata %>% 
  ggplot(aes(x = age, y = visit)) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  labs(y = "Hospital visits", x = "Age (binned)")



#(p.37)
#대역폭 2년 설정
filtered_data <- mydata %>%
  filter(age >= 19 & age <= 23)

#19~23세 시각화
filtered_data %>% 
  ggplot(aes(x = age, y = visit)) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  labs(y = "Hospital visits", x = "Age (binned)")



#(p.45)
#단순 선형회귀모형 추정
mymodel <- lm(visit ~ age_d, data = filtered_data)

summary(mymodel)

#단순 선형회귀모형 결과 시각화
filtered_data %>% 
  ggplot(aes(x = age, y = visit)) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  geom_smooth(method = "lm", color = "blue", se = FALSE) +
  labs(y = "Hospital visits", x = "Age (binned)")



#(p.47)
#RDD 회귀모형 추정
mymodel2 <- lm(visit ~ treat + age_d + treat:age_d, data = filtered_data)

summary(mymodel2)

#RDD 회귀모형 결과 시각화
filtered_data %>% 
  ggplot(aes(x = age, y = visit, color = factor(treat))) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  geom_smooth(data = subset(filtered_data, age < 21), method = "lm", color = "cornflowerblue", se = FALSE) +
  geom_smooth(data = subset(filtered_data, age >= 21), method = "lm", color = "forestgreen", se = FALSE) +
  scale_color_manual(values= c("0" = "cornflowerblue", "1" = "forestgreen"))+
  labs(y = "Hospital visits", x = "Age (binned)")



#(p.51)
#RDD 비선형 회귀모형 추정
mymodel3 <- lm(visit ~ treat + age_d + I(age_d^2) + treat:age_d + treat:I(age_d^2), data = filtered_data)

summary(mymodel3)

#RDD 비선형 회귀모형 결과 시각화
filtered_data %>% 
  ggplot(aes(x = age, y = visit, color = factor(treat))) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  geom_smooth(data = subset(filtered_data, age < 21), method = "lm", formula = y ~ x + I(x^2), color = "cornflowerblue", se = FALSE) +
  geom_smooth(data = subset(filtered_data, age >= 21), method = "lm", formula = y ~ x + I(x^2), color = "forestgreen", se = FALSE) +
  scale_color_manual(values= c("0" = "cornflowerblue", "1" = "forestgreen"))+
  labs(y = "Hospital visits", x = "Age (binned)")



#bonus
#3차항 포함
mymodel4 <- lm(visit ~ treat + age_d + I(age_d^2) + I(age_d^3) + treat:age_d + treat:I(age_d^2) + treat:I(age_d^3), data = filtered_data)

summary(mymodel4)

filtered_data %>% 
  ggplot(aes(x = age, y = visit, color = factor(treat))) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  geom_smooth(data = subset(filtered_data, age < 21), method = "lm", formula = y ~ x + I(x^2) + I(x^3), color = "cornflowerblue", se = FALSE) +
  geom_smooth(data = subset(filtered_data, age >= 21), method = "lm", formula = y ~ x + I(x^2)+ I(x^3), color = "forestgreen", se = FALSE) +
  scale_color_manual(values= c("0" = "cornflowerblue", "1" = "forestgreen"))+
  labs(y = "Hospital visits", x = "Age (binned)")


#대역폭 1.5년 설정
filtered_data_18m <- mydata %>%
  filter(age >= 19.5 & age <= 22.5)

mymodel5 <- lm(visit ~ treat + age_d + I(age_d^2) + treat:age_d + treat:I(age_d^2), data = filtered_data_18m)

summary(mymodel5)

#RDD 비선형 회귀모형 결과 시각화
filtered_data_18m %>% 
  ggplot(aes(x = age, y = visit, color = factor(treat))) + 
  geom_point() +
  geom_vline(xintercept = 21, color = "red", size = 1, linetype = "dashed") + 
  geom_smooth(data = subset(filtered_data_18m, age < 21), method = "lm", formula = y ~ x + I(x^2), color = "cornflowerblue", se = FALSE) +
  geom_smooth(data = subset(filtered_data_18m, age >= 21), method = "lm", formula = y ~ x + I(x^2), color = "forestgreen", se = FALSE) +
  scale_color_manual(values= c("0" = "cornflowerblue", "1" = "forestgreen"))+
  labs(y = "Hospital visits", x = "Age (binned)")
