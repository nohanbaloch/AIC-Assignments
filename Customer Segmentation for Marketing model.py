# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier

# Load and preprocess customer data
customer_data = pd.read_csv("customer_data.csv")
X = customer_data.drop(columns=["ID", "Age"])
y = customer_data["Var_1"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train models
linear_regression = LinearRegression()
linear_regression.fit(X_train, y_train)

logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)

random_forest = RandomForestClassifier()
random_forest.fit(X_train, y_train)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X_train)

decision_tree = DecisionTreeClassifier()
decision_tree.fit(X_train, y_train)

# Evaluate models
linear_regression_score = linear_regression.score(X_test, y_test)
logistic_regression_score = logistic_regression.score(X_test, y_test)
random_forest_score = random_forest.score(X_test, y_test)
knn_score = knn.score(X_test, y_test)
decision_tree_score = decision_tree.score(X_test, y_test)

# Print model scores
print("Linear Regression Score:", linear_regression_score)
print("Logistic Regression Score:", logistic_regression_score)
print("Random Forest Score:", random_forest_score)
print("KNN Score:", knn_score)
print("Decision Tree Score:", decision_tree_score)
