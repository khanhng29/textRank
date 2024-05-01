import matplotlib.pyplot as plt
from preprocessing import word_counts
from text_rank import text_rank_sum
from test import ori_length

# X-axis values (assuming each array corresponds to a different category)
x_values = list(range(1, 205))  # Assuming 204 values in each array

# Plotting word_counts as a bar chart
plt.figure(figsize=(10, 5))  # Adjust figure size as needed
plt.bar(x_values, word_counts, color='b', label='ori text')

# Adding labels and title for the first chart
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Word Counts Bar Chart')
plt.legend()

# Save the first plot as an image file
plt.grid(True)
plt.savefig('word_counts_bar_chart.png')
plt.show()

# Plotting text_rank_sum as a bar chart
plt.figure(figsize=(10, 5))  # Adjust figure size as needed
plt.bar(x_values, text_rank_sum, color='g', label='new sum')

# Adding labels and title for the second chart
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Text Rank Sum Bar Chart')
plt.legend()

# Save the second plot as an image file
plt.grid(True)
plt.savefig('text_rank_sum_bar_chart.png')
plt.show()

# Plotting ori_length as a bar chart
plt.figure(figsize=(10, 5))  # Adjust figure size as needed
plt.bar(x_values, ori_length, color='r', label='ori sum')

# Adding labels and title for the third chart
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Ori Length Bar Chart')
plt.legend()

# Save the third plot as an image file
plt.grid(True)
plt.savefig('ori_length_bar_chart.png')
plt.show()
