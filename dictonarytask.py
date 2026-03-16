data = {
    "Aman": [85, 90, 78],
    "Eakam": [92, 88, 95],
    "Kiran": [70, 75, 80]
}

top_student = ""
highest_avg = 0
for name in data:
    scores = data[name]
    avg = sum(scores) / len(scores)
    print(f"{name}: {round(avg, 1)}")
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

print("-" * 20)
print(f"Top Student: {top_student}")