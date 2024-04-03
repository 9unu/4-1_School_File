#p.5
#데이터 불러오기
mydata3 <-read.csv("BEDA_support2.csv", fileEncoding="euc-kr")

#데이터 둘러보기
summary(mydata3)

#선형회귀모형 분석
myresult <- lm(result ~ program + male + gpa, data = mydata3)

#선형회귀모형 분석 결과 보기
summary(myresult)



#p.7
#선형회귀모형 예측
predict(myresult, newdata = data.frame(male = c(0), program = c(1), gpa = c(4)))



#p.8
#로짓선형회귀모형 분석
myresult2 <- glm(result ~ male + program + gpa, data = mydata3, family = binomial)

#로짓선형회귀모형 분석 결과 보기 (직접 해석 X)
summary(myresult2)

#로짓선형회귀모형 예측
predict(myresult2, newdata = data.frame(male = c(0), program = c(1), gpa = c(4)), type = "response")

#로짓선형회귀모형 예측 - 복수
predict(myresult2, newdata = data.frame(male = c(0,0), program = c(1,0), gpa = c(4,4)), type = "response")



#p.9
#PSM 매칭 시행
mymodel3 <- matchit (program ~ male + gpa,
                     data = mydata3,
                     distance = "glm",
                     method = "nearest")

#매칭 결과 요약
summary(mymodel3)



#p.10
#매칭 데이터 추출
matched_data3 <- match.data(mymodel3) 

#매칭 데이터 요약
summary(matched_data3)

#인과성 분석
with(matched_data3, t.test(result ~ program))
