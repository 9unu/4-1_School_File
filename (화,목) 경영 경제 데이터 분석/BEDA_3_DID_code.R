#(p.33)
#데이터 불러오기
mydata <- read.csv("BEDA_3_DID_data_cardkrueger.csv")

#처음 몇 줄 보기
head(mydata)

#기초통계량 보기
summary(mydata)



#(p.34)
#관련 패키지 설치 및 불러오기
install.packages("dplyr")
library(dplyr)

#처치군/대조군 및 처치 이전/이후 기준으로 emp 평균치 계산 
mydata %>% 
  mutate(group = paste0(treat, after)) %>%
  group_by(group) %>%
  summarise(mean_outcome = mean(emp, na.rm = TRUE))



#(p.35)
#그룹별 체인점 유형 수 및 비중
mydata %>% 
  mutate(group = paste0(treat, after)) %>%
  group_by(group, chain) %>%
  summarise(count = n()) %>%
  mutate(proportion = count / sum(count))



#(p.42)
#이중차분분석
mydid <- lm (emp ~treat + after + treat:after, data = mydata)
summary(mydid)



#(p.51)
#통제변수를 포함한 이중차분분석
mydid2 <- lm (emp ~treat + after + treat:after + factor(chain), data = mydata)
summary(mydid2)



  
