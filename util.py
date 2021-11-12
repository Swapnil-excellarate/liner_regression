from math import sqrt

def mean(value):
    return sum(value)/float(len(value))

def variance(values, mean):
    return sum([(x-mean)**2 for x in values])

def covariance(x, x_mean, y, y_mean):
    covar=0.0
    for i in range(len(x)):
        covar += (x[i] - x_mean)*(y[i] - y_mean)
    return covar

def coefficients(dataset):
    x=[row[0] for row in dataset]
    y=[row[1] for row in dataset]
    x_mean, y_mean=mean(x), mean(y)
    b1=covariance(x, x_mean, y, y_mean)/variance(x, x_mean)
    b0=y_mean-b1*x_mean
    return[b0, b1]

class liner_regression_class:
    def rmse(self, actul, predicted):
        sum_error=0.0
        for i in range(len(actul)):
            prediction_error=predicted[i]-actul[i]
            sum_error += (prediction_error**2)
        mean_error= sum_error/float(len(actul))
        return sqrt(mean_error)

    def algo(self, dataset, algoritham):
        test=list()
        for row in dataset:
            rows=list(row)
            rows[-1] = None
            test.append(rows)
        predicted=algoritham(dataset, test)
        print(predicted)
        actual=[row[-1] for row in dataset]
        rmse=self.rmse(actual, predicted)
        return rmse

    def liner_regression(self, train, test):
        prediction=list()
        b0, b1 = coefficients(train)
        for row in test:
            y=b0 + b1 * row[0]
            prediction.append(y)
        return prediction

#calculate mean and variance 
dataset=[[1,2],[2,3],[1,3],[4,2],[5,3]]
x=[row[0] for row in dataset]
y=[row[1] for row in dataset]

x_mean, y_mean=mean(x), mean(y)
x_variance, y_variance=variance(x, x_mean), variance(y, y_mean)
covar=covariance(x, x_mean, y, y_mean)
print('x status : mean=%.3f variance=%.3f' %(x_mean, x_variance))
print('y status : mean=%.3f variance=%.3f' %(y_mean, y_variance))
print('covariance is %.3f' %(covar))

c1=liner_regression_class()
rmse=c1.algo(dataset, c1.liner_regression)
print('rmse : %3f'% (rmse))
