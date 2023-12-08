import matplotlib.pyplot as plt

# Sample data
counts = [1200, 2200]  # Replace with your actual counts
international_plan_labels = ['No', 'Yes']  # Replace with your actual row names

# Bar plot
plt.bar(international_plan_labels, counts, color=["blue", "red"])
plt.ylim(0, 3300)
plt.ylabel("Count")
plt.xlabel("International Plan")
plt.title("Comparison Bar Chart: Churn Proportions by International Plan")

# Show the plot
plt.show()