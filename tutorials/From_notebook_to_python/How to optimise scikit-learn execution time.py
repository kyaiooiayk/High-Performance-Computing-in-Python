#!/usr/bin/env python
# coding: utf-8

# # Introduction

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# **What?** How to opptimise scikit-learn execution  time
# 
# <br></font>
# </div>

# # What options do we have?

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - **Option #1** = Changing your optimization function (solver)
# - **Option #2** = Using different hyperparameter optimization techniques (grid search, random search, early stopping)
# - **Option #3** = Parallelize or distribute your training with joblib and Ray
# 
# 
# <br></font>
# </div>

# # Import modules

# In[ ]:


import time
from IPython.display import Markdown
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from tune_sklearn import TuneGridSearchCV
from sklearn.model_selection import GridSearchCV
import numpy as np
import time
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
import warnings
warnings.filterwarnings("ignore")



# # Helper function

# In[ ]:


def myPrint(string, c = "blue"):    
    """My version of the python-native print command.
    
    Print in bold and red tect
    """
    colorstr = "<span style='color:{}'>{}</span>".format(c, '**'+ string + '**' )    
    display(Markdown(colorstr))


# # Option #1 - Changing optimisation solver

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - A **full gradient** algorithm (liblinear) converges rapidly, but each iteration can be prohibitively costly because it requires you to use all of the data. 
# - A **sub-sampled** approach each iteration is cheap to compute, but it can converge much more slowly. 
# - **Saga** algorithms achieve the best of both worlds. Each iteration is cheap to compute, and the algorithm converges rapidly because of a variance reduction technique. 
# - It is important to note that quick convergence doesn’t always matter in practice and different solvers suit different problems.
# 
# 
# - The we are performing below shows that the results depends on the sample size.
# 
# <br></font>
# </div>

# In[ ]:


# Solvers
solvers = ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]
samples = [1000, 10000, 100000]

for sample in samples:
    print("=====================")
    print("Sample size: ", sample)
    X, y = make_classification(n_samples=sample, n_features=int(0.01*sample), n_classes = 2)

    # Set training and validation sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = int(0.1*sample))

    bestTime = 1.e6
    bestSolver = "dummy"
    for sol in solvers: 
        print("Currently using solver: ", sol)
        start = time.time()
        logreg = LogisticRegression(solver=sol)
        logreg.fit(X_train, y_train)
        end = time.time()
        print(sol + " Fit Time: ",end-start)
        if end-start < bestTime:
            bestSolver = sol
            bestTime = end-start

        if sol == solvers[-1]:
            myPrint("Best:--->" + bestSolver)


# # Option #2 = Using different hyperparameter optimization techniques 

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - GridSearchCV and RandomizedSearchCV are all good old options but the newly added HalvingGridSearchCV and HalvingRandomSearch are even better especially for saving in time they offer.
# - While these new techniques are exciting, there is a library called **Tune-sklearn** that provides cutting edge hyperparameter tuning techniques (bayesian optimization, early stopping, and distributed execution) that can provide significant speedups over grid search and random search.
# - There is  support also for Skorch (PyTorch), KerasClassifiers (Keras), and XGBoostClassifiers (XGBoost).
# - Scalability: The library leverages **Ray Tune**, a library for distributed hyperparameter tuning, to efficiently and transparently parallelize cross validation on multiple cores and even multiple machines.
# 
# 
# - We'll show here a simple examples withL
#     - `from tune_sklearn import TuneGridSearchCV`
#     - `from sklearn.model_selection import GridSearchCV`
# 
# <br></font>
# </div>

# **Dataset and hyperparameter space**

# In[ ]:


# Set training and validation sets
X, y = make_classification(n_samples=11000, n_features=1000, n_informative=50, n_redundant=0, n_classes=10, class_sep=2.5)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1000)

# Example parameters to tune from SGDClassifier
parameters = {
    'alpha': [1e-4, 1e-1, 1],
    'epsilon':[0.01, 0.1]
}


# **Tune-skleanr**

# In[ ]:


tune_search = TuneGridSearchCV(
    SGDClassifier(),
    parameters,
    early_stopping="MedianStoppingRule",
    max_iters=10
)

start = time.time()
tune_search.fit(X_train, y_train)
end = time.time()
print("Tune Fit Time:", end - start)
pred = tune_search.predict(X_test)
accuracy = np.count_nonzero(np.array(pred) == np.array(y_test)) / len(pred)
print("Tune Accuracy:", accuracy)


# **sklearn**

# In[ ]:


# n_jobs=-1 enables use of all cores like Tune does
sklearn_search = GridSearchCV(
    SGDClassifier(),
    parameters,
    n_jobs = -1
)

start = time.time()
sklearn_search.fit(X_train, y_train)
end = time.time()
print("Sklearn Fit Time:", end - start)
pred = sklearn_search.predict(X_test)
accuracy = np.count_nonzero(np.array(pred) == np.array(y_test)) / len(pred)
print("Sklearn Accuracy:", accuracy)


# # Option #3 = Parallelize or distribute your training with joblib and Ray

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# - Another way to increase your model building speed is to parallelize or distribute your training with joblib and Ray. By **default**, scikit-learn trains a model using a single core. 
# - It is important to note that virtually all computers today have multiple cores. 
# - Scikit-Learn can parallelize training on a single node with joblib which by default uses the **loky** backend. Joblib allows you to choose between backends like ‘loky’, ‘multiprocessing’, ‘dask’, and ‘ray’. This is a great feature as the ‘loky’ backend is optimized for a single node and not for running distributed (multinode) applications.
# 
# <br></font>
# </div>

# ![image.png](attachment:image.png)

# <div class="alert alert-block alert-info">
# <font color=black><br>
# 
# -  Running distributed applications can introduce a host of complexities like:
#     - Scheduling tasks across multiple machines
#     - Transferring data efficiently
#     - Recovering from machine failures
# - Ray backend can handle these details for you, keep things simple, and give you better performance.
# 
# <br></font>
# </div>

# ![image.png](attachment:image.png)

# # References

# <div class="alert alert-block alert-warning">
# <font color=black><br>
# 
# - [Article](https://medium.com/distributed-computing-with-ray/how-to-speed-up-scikit-learn-model-training-aaf17e2d1e1)
# - [Code on changing solvers](https://gist.github.com/mGalarnyk/f42f434fc162be108a3bb5bc36464a59) 
# - [Examples of how to use tune-sklearn]()https://github.com/ray-project/tune-sklearn/tree/master/examples
# <br></font>
# </div>

# In[ ]:




