from collections import Counter

colors = ['red', 'blue', 'green', 'blue', 'red', 'red', 'yellow', 'blue', 'green', 'blue']
color_counts = Counter(colors)
mean_color = color_counts.most_common(1)[0][0]# the most common color
#most worn color
most_common_color = color_counts.most_common(1)[0][0]
#median color
sorted_colors = sorted(colors)
median_color = sorted_colors[len(sorted_colors) // 2]
#prbability red
total_color = len(colors)
red_count = colors.count('red')
probability_red = red_count / total_color

print(f"the median color is: {mean_color}")
print(f"the most worn color is: {most_common_color}")
print(f"the mean color is: {mean_color}")
print(f"the probability of choosing red is: {probability_red}")