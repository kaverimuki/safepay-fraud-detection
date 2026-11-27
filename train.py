import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

print("Model training started...")

# 1000 fake transaction data create panrom
np.random.seed(42)
data = []
for i in range(1000):
    amount = np.random.randint(10, 100000)
    time = np.random.randint(0, 24)
    is_foreign = np.random.choice([0, 1])

    # Fraud rule - itha vachu thaan model kathukum
    if amount > 50000 or (is_foreign == 1 and amount > 20000):
        fraud = 1
    else:
        fraud = 0
    data.append([amount, time, is_foreign, fraud])

df = pd.DataFrame(data, columns=["amount", "time", "is_foreign", "fraud"])

X = df[["amount", "time", "is_foreign"]]
y = df["fraud"]

model = RandomForestClassifier()
model.fit(X, y)

# Model ah save panrom
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Training mudinjiduchu! model.pkl create aayiduchu")