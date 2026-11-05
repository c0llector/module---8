TP = 21
FP = 9
FN = 3
TN = 27

total = TP + FP + FN + TN

accuracy = (TP + TN) / total
precision = TP / (TP + FP)
recall = TP / (TP + FN)

f1 = 2 * precision * recall / (precision + recall)

print("Қателер матрицасы:")
print(f"Дұрыс анықталған жоғары сұраныс: {TP}")
print(f"Қате анықталған жоғары сұраныс: {FP}")
print(f"Байқалмай қалған жоғары сұраныс: {FN}")
print(f"Дұрыс анықталған төмен сұраныс: {TN}")

print("\nМодельді бағалау нәтижелері:")
print(f"Жалпы дәлдік: {accuracy:.1%}")
print(f"Оң болжамдардың дәлдігі: {precision:.1%}")
print(f"Толықтық: {recall:.1%}")
print(f"F1 көрсеткіші: {f1:.1%}")

TP2 = 0
FP2 = 0
FN2 = 5
TN2 = 45

accuracy2 = (TP2 + TN2) / (TP2 + TN2 + FP2 + FN2)
recall2 = TP2 / (TP2 + FN2)

print("\nЕкінші мысал:")
print(f"Дұрыс жоғары болжам: {TP2}")
print(f"Қате жоғары болжам: {FP2}")
print(f"Байқалмай қалған жоғары сұраныс: {FN2}")
print(f"Дұрыс төмен болжам: {TN2}")
print(f"Жалпы дәлдік: {accuracy2:.1%}")
print(f"Толықтық: {recall2:.1%}")