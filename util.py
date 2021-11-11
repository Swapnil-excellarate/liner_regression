

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
