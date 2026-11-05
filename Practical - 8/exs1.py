p_high = 6 / 12
p_low = 6 / 12

p_cold_high = 5 / 6
p_rain_high = 4 / 6

p_cold_low = 2 / 6
p_rain_low = 1 / 6

score_high = p_high * p_cold_high * p_rain_high
score_low = p_low * p_cold_low * p_rain_low

total = score_high + score_low

posterior_high = score_high / total
posterior_low = score_low / total

print("Суық және жаңбырлы күн:")
print(f"Жоғары сұраныс: {score_high:.5f}")
print(f"Төмен сұраныс: {score_low:.5f}")
print(f"Жоғары сұраныс ықтималдығы: {posterior_high:.1%}")
print(f"Төмен сұраныс ықтималдығы: {posterior_low:.1%}")

score_high_no_rain = p_high * p_cold_high * (1 - p_rain_high)
score_low_no_rain = p_low * p_cold_low * (1 - p_rain_low)

total2 = score_high_no_rain + score_low_no_rain

print("\nСуық, бірақ жаңбырсыз күн:")
print(f"Жоғары сұраныс ықтималдығы: {score_high_no_rain / total2:.1%}")
print(f"Төмен сұраныс ықтималдығы: {score_low_no_rain / total2:.1%}")

p_event_1 = (0 + 1) / (6 + 2)
p_event_0 = (6 + 1) / (6 + 2)

print(' ')
print(f"Оқиғаның болу ықтималдығы: {p_event_1:.1%}")
print(f"Оқиғаның болмау ықтималдығы: {p_event_0:.1%}")