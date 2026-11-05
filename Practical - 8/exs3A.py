import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([100, 150, 200, 250, 300])
X = X.reshape(-1, 1)

y = np.array([29, 41, 53, 66, 78])

model = LinearRegression()
model.fit(X, y)

w = model.coef_[0]
b = model.intercept_

print("Сызықтық регрессия нәтижелері:")
print(f"Көлбеулік коэффициенті: {w:.3f}")
print(f"Бос мүше: {b:.2f}")

print(f"Модель теңдеуі: y = {w:.3f}x + {b:.2f}")

prediction = model.predict([[180]])
print(f"180 келуші үшін болжам: {prediction[0]:.2f}")

X_first = np.array([[100], [150]])
y_first = np.array([29, 41])

y_pred = model.predict(X_first)

residuals = y_first - y_pred
mse = np.mean(residuals ** 2)

print("\nАлғашқы екі бақылау:")
print("Болжанған мәндер:", y_pred)
print("Қалдық қателер:", residuals)
print(f"Орташа квадраттық қате: {mse:.3f}")

pred_A = 0.20 * X_first.flatten() + 10
pred_B = 0.25 * X_first.flatten() + 5

mse_A = np.mean((y_first - pred_A) ** 2)
mse_B = np.mean((y_first - pred_B) ** 2)

print("\nЕкі модельді салыстыру:")
print("А моделінің болжамдары:", pred_A)
print(f"А моделінің қатесі: {mse_A:.3f}")

print("B моделінің болжамдары:", pred_B)
print(f"B моделінің қатесі: {mse_B:.3f}")

if mse_A < mse_B:
    print("Жақсырақ модель: A")
else:
    print("Жақсырақ модель: B")