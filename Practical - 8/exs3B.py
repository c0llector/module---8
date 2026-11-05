import numpy as np

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

X_train = np.array([
    [1, 1], [1, 1], [1, 1],
    [1, 0], [1, 0], [0, 1],
    [1, 1], [1, 0], [0, 0],
    [0, 0], [0, 0], [0, 0]
])

y_train = np.array([
    1, 1, 1, 1, 1, 1,
    0, 0, 0, 0, 0, 0
])

X_test = np.array([
    [1, 1],
    [1, 0]
])

model = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)

model.fit(X_train, y_train)

p = model.predict_proba(X_test)[:, 1]
alerts = (p >= 0.50).astype(int)

print("Жоғары сұраныстың ықтималдықтары:")
print(p)

print("\nБолжанған кластар:")
print(alerts)

print("\nТолық нәтижелер:")

for i in range(len(X_test)):
    print(f"Ауа райы белгілері: {X_test[i]}")
    print(f"Жоғары сұраныс ықтималдығы: {p[i]:.1%}")
    print(f"Болжанған класс: {alerts[i]}")
    print()

nb_high = 10 / 11

print("Наив Байес нәтижесі:", f"{nb_high:.1%}")
print("Логистикалық регрессия нәтижесі:", f"{p[0]:.1%}")