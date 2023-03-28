import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split


X, y = make_classification(
    n_samples=200,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=213,
    n_clusters_per_class=1,
    class_sep=1,
)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

plt.figure()
plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=y_train, cmap="coolwarm")
plt.scatter(x=X_test[:, 0], y=X_test[:, 1], c=y_test, cmap="coolwarm", marker="x")
plt.show()

from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

print("Koeficijenti:", logreg.coef_)
print("Presječna točka: ", logreg.intercept_)

arr = []
for x in X_train[:, 0]:
    y = logreg.intercept_ + x * logreg.coef_[0][0] / (-logreg.coef_[0][1])
    arr.append(y)

plt.plot(X_train[:, 0], arr)
plt.scatter(x=X_train[:, 0], y=X_train[:, 1], c=y_train, cmap="coolwarm")
plt.show()

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    accuracy_score,
    precision_score,
    recall_score,
)

y_pred = logreg.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Matrica zabune:")
print(cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
print("Točnost: {:.2f}".format(accuracy))
print("Preciznost: {:.2f}".format(precision))
print("Odziv: {:.2f}".format(recall))

correctly_classified = y_test == y_pred
plt.scatter(
    X_test[correctly_classified, 0],
    X_test[correctly_classified, 1],
    c="green",
    marker="o",
)

incorrectly_classified = y_test != y_pred
plt.scatter(
    X_test[incorrectly_classified, 0],
    X_test[incorrectly_classified, 1],
    c="black",
    marker="x",
)
plt.show()
