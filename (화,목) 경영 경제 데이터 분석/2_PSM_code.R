#(p.25)
#MatchIt 패키지 설치
install.packages("MatchIt")

#MatchIt 패키지 불러오기
library(MatchIt)

#작업 경로 설정 - 실행 X
setwd("파일 경로")

#파일 불러오기 (csv파일) - 실행 X
mydata <-read.csv("파일명", fileEncoding="euc-kr")

#라이브러리 제공 기본 데이터(lalonde) 불러오기 및 해당 데이터를 mydata에 저장
data("lalonde")
mydata <- lalonde



#(p.28)
#맨 위 몇 줄 보기
head(mydata)

#자료 구조 보기
str(mydata)

#주요 통계량 보기
summary(mydata)




#(p.34)
#matchit 함수 활용
mymodel <- matchit (treat ~ age + educ + married + re74,
                    data = mydata,
                    distance = "glm",
                    method = "nearest")

#logit 모형 추정 결과 불러오기 (psm 결과가 저장된 mymodel이라는 변수 내 model 부분)
summary(mymodel$model)



#(p.35)
#glm을 이용한 logit model 추정
logitmodel <- glm(treat ~ age + educ + married + re74, data = mydata, family = binomial)

#추정 결과 요약
summary(logitmodel)



#(p.41)
#이전에 추정한 mymodel의 summary 출력
summary(mymodel)



# (p.44)
#전체 대조군과 매칭된 대조군의SMD 값을 시각화하여 비교해보자
plot(summary(mymodel))



#(p.46)
#성향점수 분포를 jitter된 시각화 자료로 살펴보자
plot(mymodel, type = "jitter")

#성향점수 분포를 히스토그램으로 나타내어보자
plot(mymodel, type = "hist")



#(p.48)
#매칭된 데이터 분리
matched_data <- match.data(mymodel) 

#매칭된 데이터 대상 t-검정 수행
with(matched_data, t.test(re78 ~ treat))



#(p.50)
#매칭된 데이터 살펴보기 
head(matched_data)

#매칭된 데이터 기초 통계량 검토
summary(matched_data)

#매칭된 데이터를 csv 파일로 빼내기
write.csv(matched_data, file = "matched_data_lalonde.csv")




#Quick Review
#(p.57)
#데이터 불러오기
mydata2 <- read.csv("BEDA_2_PSM_data.csv")

#데이터 둘러보기
summary(mydata2)



#(p.58)
#matchit 함수 활용
mymodel2 <- matchit (treat ~ gender + age + h_income + h_mem + elec_bill,
                    data = mydata2,
                    distance = "glm",
                    method = "nearest")

#주요 결과 산출 
summary(mymodel2)



#(p.59)
#주요 시각화 분석 시행
plot(summary(mymodel2))

plot(mymodel2, type = "jitter")

plot(mymodel2, type = "hist")



#(p.60)
#매칭 데이터 구성
matched_data2 <- match.data(mymodel2) 

#카이제곱 검정을 위한 테이블 구성
table_for_test <- table(matched_data2$treat, matched_data2$tou_intent)

#카이제곱 검정
chisq.test(table_for_test)

#매칭된 데이터를 csv 파일로 빼내기
write.csv(matched_data2, file = "matched_data_beda1.csv")


