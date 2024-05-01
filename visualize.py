import matplotlib.pyplot as plt
from preprocessing import word_counts
from text_rank import text_rank_sum
from test import ori_length

# X-axis values (assuming each array corresponds to a different category)
x_values = list(range(1, 205))  # Assuming 204 values in each array

# Plotting
plt.plot(x_values, word_counts, marker='o', label='ori text')
plt.plot(x_values, text_rank_sum, marker='s', label='new sum')
plt.plot(x_values, ori_length, marker='^', label='ori sum')

# Adding labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Graph')

# Adding legend
plt.legend()

# Save plot as an image file
plt.grid(True)
plt.savefig('line_graph.png')

# Show plot
plt.show()
