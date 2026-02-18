employees = {
    "Ravi": 92,
    "Anita": 88,
    "Kiran": 92,
    "Suresh": 85
}
highest_score = max(employees.values())
top_performers = []

for name, score in employees.items():
    if score == highest_score:
        top_performers.append(name)
print("Top Performers Eligible for Bonus:", ", ".join(top_performers), f"(Score: {highest_score})")
