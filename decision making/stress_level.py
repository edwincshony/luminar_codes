"""
6)Stress Level Indicator
    Input: stress_score (1 to 10)
    Conditions:
    If score between 1 and 3 → Low Stress
    If score between 4 and 6 → Moderate Stress
    If score between 7 and 10 → High Stress
"""

stress_score = int(input("stress score: "))

if stress_score >= 1 and stress_score <= 3:
    print("Low Stress")
elif stress_score >= 4 and stress_score <= 6:
    print("Moderate Stress")
elif stress_score >= 7 and stress_score <= 10:
    print("High Stress")
else:
    print("invalid")