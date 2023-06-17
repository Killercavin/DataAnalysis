from matplotlib import pyplot as plt
from random_walk import RandomWalk

# Make a randomn walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the random walk
plt.title('RANDOM WALK PLOT')
plt.style.use('classic')
plt.scatter(rw.x_values, rw.y_values)
plt.show()
plt.savefig('random_walk.png', bbox_inches='tight')