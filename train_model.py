import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data.csv")

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

model = RandomForestClassifier(n_estimators=200)
model.fit(X, y)

accuracy = model.score(X, y)
print(f"Accuracy: {accuracy}")

joblib.dump(model, "gesture_model.pkl")
print(" Model Saved")