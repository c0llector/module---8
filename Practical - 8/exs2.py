p_high = 10 / 11
p_low = 1 - p_high

actions = {
    'Extra': ([p_high, p_low], [0, -60]),
    'Usual': ([p_high, p_low], [-30, 0])
}

def EU(probs, utilities):
    return sum(p * u for p, u in zip(probs, utilities))

scores = {
    name: EU(*values)
    for name, values in actions.items()
}

names = {
    "Extra": "Қосымша дайындау",
    "Usual": "Әдеттегі мөлшер"
}

print("Күтілетін пайдалылықтар:")
for name, utility in scores.items():
    print(f"{names[name]}: {utility:.2f}")

best = max(scores, key=scores.get)

print("\nЕң тиімді әрекет:")
print(names[best])

print("\nКүтілетін шығындар:")
for name, utility in scores.items():
    print(f"{names[name]}: {-utility:.2f}")

threshold = 2 / 3

print(f"\nҚосымша дайындау шегі: {threshold:.1%}")

for weather, p in [
    ("Суық және жаңбырлы күн", 10 / 11),
    ("Суық, жаңбырсыз күн", 0.5)
]:
    loss_extra = (1 - p) * 60
    loss_usual = p * 30

    if loss_extra < loss_usual:
        decision = "Қосымша дайындау"
    elif loss_usual < loss_extra:
        decision = "Әдеттегі мөлшер"
    else:
        decision = "Екі әрекет тең"

    print(f"{weather}: {decision}")