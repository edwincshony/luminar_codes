"""
Fitness App Step Goal
Problem Statement 
A fitness app records the user’s daily steps. The goal is 10,000 steps. Write a program that keeps asking for daily steps until total steps ≥10,000. Print total steps and days taken.
Input Format Daily steps as integers.
Output Format Total steps and days taken to reach the goal.
Sample Input:
3000
4000
3500
Sample Output:
Goal reached! Total steps: 10500 in 3 days.
"""

tot_steps = 0

count = 0

while True:

    steps = int(input())

    tot_steps += steps

    count += 1

    if tot_steps >= 10000:

        print(f"Goal reached! Total steps: {tot_steps} in {count} days.")

        break