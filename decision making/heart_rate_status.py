"""
3)Heart Rate Status
    Input: heart_rate (beats per minute)
    Conditions:
    If heart_rate < 60 → Low Heart Rate
    If heart_rate between 60 and 100 → Normal
    If heart_rate > 100 → High Heart Rate
"""

heart_rate = int(input("enter heart rate: "))

if heart_rate < 60:
    print("Low Heart Rate")
elif heart_rate <= 100:
    print("Normal")
elif heart_rate > 100:
    print("High Heart Rate")

    
    
