import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import joblib

# SAMPLE DATASET (replace with real dataset later)
data = pd.DataFrame([
    [10, 2, 1, 0],
    [20, 3, 2, 0],
    [50, 5, 4, 1],
    [80, 7, 6, 1],
    [30, 2, 3, 0],
    [60, 6, 5, 1],
    [90, 8, 7, 1],
    [15, 1, 1, 0],
], columns=["loc", "complexity", "coupling", "label"])

X = data[["loc", "complexity", "coupling"]]
y = data["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# MODEL
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# PREDICTION
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

train_acc = accuracy_score(y_train, y_train_pred)
test_acc = accuracy_score(y_test, y_test_pred)

print("Train Accuracy:", train_acc)
print("Test Accuracy:", test_acc)

# SAVE MODEL
joblib.dump(model, "quality_model.pkl")

# ==========================
# 📊 ACCURACY GRAPH
# ==========================
labels = ["Train Accuracy", "Test Accuracy"]
values = [train_acc * 100, test_acc * 100]

plt.figure(figsize=(6, 4))
plt.bar(labels, values)
plt.title("Model Accuracy Graph")
plt.ylabel("Accuracy %")
plt.ylim(0, 100)

plt.savefig("accuracy_graph.png")
plt.show()