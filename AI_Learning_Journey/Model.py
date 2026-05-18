# ====== 1. IMPORTS ======
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.tree import plot_tree

# ====== 2. LOAD DATA ======
# Replace   this with your own file later
data = pd.read_csv("/home/zentinely2k/Documents/Y2K-Zone/Code-Playground/AI_Learning_Journey/DataBase.csv")

# ====== 3. SELECT FEATURES & LABEL ======
# Features = inputs
X = data[["feature1","feature2","feature3","feature4"]]

# Labels = what you want to predict
y = data["label"]

# ====== 4. SPLIT DATA ======
X_train,  X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ====== 5. SCALE DATA ======
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ====== 6. CREATE MODEL ======
model = DecisionTreeClassifier()

# ====== 7. TRAIN ======
model.fit(X_train, y_train)

# ====== 8. PREDICT ======
y_pred = model.predict(X_test)

# ====== 9. EVALUATE ======
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# ====== 10. TEST WITH YOUR OWN INPUT ======
# Example: change these values
new_data = [[172,14,0,0]]

new_data = scaler.transform(new_data)
prediction = model.predict(new_data)

print("Prediction:", prediction)

X_vis = data[["feature1", "feature2"]]
y = data["label"]

def decision_tree():
   plt.figure(figsize=(12,8))
   plot_tree(model, filled=True)
   plt.show()

def see_graph_dots():
   plt.scatter(X_vis["feature1"], X_vis["feature2"], c=y)
   plt.xlabel("feature1")
   plt.ylabel("feature2")
   plt.title("Data Distribution")
   plt.show()

see_graph_dots()