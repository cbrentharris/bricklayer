from collections import OrderedDict
import pandas
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import preprocessing
import numpy as np

class Classifier(object):
    MODELS = OrderedDict([
        ('LR', LogisticRegression()),
        ('LDA', LinearDiscriminantAnalysis()),
        ('CART', DecisionTreeClassifier()),
        ('KNN', KNeighborsClassifier()),
        ('NB', GaussianNB()),
        ('K Neighbors', KNeighborsClassifier(3)),
        ('SVM Linear', SVC(kernel="linear", C=0.025)),
        ('SVM Gamma', SVC(gamma=2, C=1)),
        ('GaussianProcessClassifier', GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True)),
        ('Decision Tree Classifier', DecisionTreeClassifier(max_depth=5)),
        ('Random Forest Classifier', RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)),
        ('MLP Classifier', MLPClassifier(alpha=1)),
    ])

    @classmethod
    def score(cls, filename):
        names = ['SLOC', 'COMMENTS', 'UDFS', 'LEVEL', 'SUBMISSION', 'GRADE']
        dataframe = pandas.read_csv(filename, names=names)
        array = dataframe.values
        X = array[:, 0:5]
        Y = array[:, 5]
        seed = 7
        results = []
        scoring = 'precision'
        lb = preprocessing.LabelBinarizer()
        lb.fit(Y)
        y_train = np.array([number[0] for number in lb.fit_transform(Y)])

        for name, model in cls.MODELS.iteritems():
            kfold = model_selection.KFold(n_splits=10, random_state=seed)
            cv_results = model_selection.cross_val_score(model, X, y_train, cv=kfold, scoring=scoring)
            results.append(cv_results)
            msg = "%s: %f (%f) (%f)" % (name, cv_results.mean(), cv_results.std(), cv_results.max())
            print(msg)
