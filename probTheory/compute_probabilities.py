"""
Probability theory - Compute probabilities
"""
# import libraries
import matplotlib.pyplot as plt
import numpy as np

# counts of the different events
c = np.array([1, 2, 4, 3])

# convert to probability (%)
prob = 100*c / np.sum(c)
print(prob)


# Taking balls out of a jar

# colored balls counts
red = 35
blue = 30
green = 45
total_balls = red + blue + green
# put them all in a jar
jar = np.hstack((1*np.ones(red), 2*np.ones(blue), 3*np.ones(green)))

# now we take 500 balls (with replacement)
num_draws = 500
num_colors = np.zeros(num_draws)

for draws in range(num_draws):
    rand_balls = int(np.random.rand()*len(jar))  # generate a random int to draw

    num_colors[draws] = jar[rand_balls]  # store the color of that balls

# now we need to know the proportion of colors drawn
prop_red = sum(num_colors == 1) / num_draws
prop_blue = sum(num_colors == 2) / num_draws
prop_green = sum(num_colors == 3) / num_draws

# plot those against the theoretical probabillity
plt.bar([1, 2, 3], [prop_red, prop_blue, prop_green], label='Proportion')
plt.plot([0.5, 1.5], [red/total_balls, red/total_balls], 'b', linewidth=3, label='Probability')
plt.plot([1.5, 2.5], [blue/total_balls, blue/total_balls], 'b', linewidth=3)
plt.plot([2.5, 3.5], [green/total_balls, green/total_balls], 'b', linewidth=3)

plt.xticks([1, 2, 3], labels=('red', 'blue', 'green'))
plt.xlabel('Balls color')
plt.ylabel('Proportion/probability')
plt.show()

