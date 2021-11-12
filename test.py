from sklearn import datasets
from util import liner_regression_class
from sklearn.model_selection import train_test_split

iris=datasets.load_iris()

x, y = iris.data, iris.target

X_train, X_test, Y_train, Y_test=train_test_split(x, y, test_size=0.2, random_state=1)

clf=liner_regression_class()
rmse=clf.algo(X_train, clf.liner_regression)
print(rmse)