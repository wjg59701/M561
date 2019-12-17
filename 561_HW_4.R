# Bill Griffin
# M561
#
# Homework 4
# 12/6/19

D = read.csv("flights.csv",colClasses=c(rep("NULL",4),NA,rep("NULL",6),NA,rep("NULL",19)),nrows=100000)
head(D)

lm.delay <- lm(DEPARTURE_DELAY ~ AIRLINE, data = D) 
summary(lm.delay)

# OUTPUT ---->

'''

> summary(lm.delay)

Call:
lm(formula = DEPARTURE_DELAY ~ AIRLINE, data = D)

Residuals:
Min      1Q  Median      3Q     Max 
-56.71  -23.39  -13.11    4.73 1356.11 

Coefficients:
Estimate Std. Error t value Pr(>|t|)    
(Intercept)  23.8892     0.4732  50.486  < 2e-16 ***
AIRLINEAS   -16.8309     0.9749 -17.264  < 2e-16 ***
AIRLINEB6    -5.4000     0.8151  -6.625 3.49e-11 ***
AIRLINEDL   -12.9368     0.6169 -20.971  < 2e-16 ***
AIRLINEEV    -1.5009     0.6494  -2.311  0.02082 *  
AIRLINEF9     9.3631     1.2555   7.458 8.88e-14 ***
AIRLINEHA   -15.3590     1.3327 -11.524  < 2e-16 ***
AIRLINEMQ    10.0155     0.7759  12.908  < 2e-16 ***
AIRLINENK     3.6576     1.1704   3.125  0.00178 ** 
AIRLINEOO    -3.1767     0.6543  -4.855 1.21e-06 ***
AIRLINEUA     0.3816     0.6858   0.556  0.57791    
AIRLINEUS   -12.7760     0.7223 -17.687  < 2e-16 ***
AIRLINEVX   -15.9414     1.4881 -10.712  < 2e-16 ***
AIRLINEWN    -2.3309     0.5674  -4.108 4.00e-05 ***
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

Residual standard error: 45.37 on 97688 degrees of freedom
(2298 observations deleted due to missingness)
Multiple R-squared:  0.02074,	Adjusted R-squared:  0.02061 
F-statistic: 159.2 on 13 and 97688 DF,  p-value: < 2.2e-16


'''

# Note P-value 2.2 x 10^-16 extremely significant result

(confidenceIntervals <- confint(lm.delay))

# Compute and print confidence intervals

# OUTPUT ---->

'''
> (confidenceIntervals <- confint(lm.delay))
                  2.5 %      97.5 %
(Intercept)  22.9617265  24.8165830
AIRLINEAS   -18.7417232 -14.9201021
AIRLINEB6    -6.9975247  -3.8023984
AIRLINEDL   -14.1459239 -11.7276818
AIRLINEEV    -2.7736945  -0.2280653
AIRLINEF9     6.9023858  11.8239038
AIRLINEHA   -17.9711249 -12.7468529
AIRLINEMQ     8.4946925  11.5362942
AIRLINENK     1.3635481   5.9516836
AIRLINEOO    -4.4590583  -1.8942512
AIRLINEUA    -0.9624857   1.7256482
AIRLINEUS   -14.1917619 -11.3602090
AIRLINEVX   -18.8580954 -13.0246629
AIRLINEWN    -3.4429495  -1.2187553
'''

prediction <- predict(lm.delay,D, interval = "predict") 
head(prediction)

# OUTPUT ---->

'''

> prediction <- predict(lm.delay,D, interval = "predict")
> head(prediction)
fit       lwr       upr
1  7.058242 -81.87939  95.99588
2 23.889155 -65.03763 112.81593
3 11.113169 -77.81521 100.04155
4 23.889155 -65.03763 112.81593
5  7.058242 -81.87939  95.99588
6 10.952352 -77.97298  99.87768


'''






