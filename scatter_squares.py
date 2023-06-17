import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-bright')

""" fig, ax = plt.subplots()
ax.scatter(2,4)
plt.show() """

plt.subplot()
y_values = [1, 2, 3, 4, 5]
x_values = [1, 4, 9, 16, 25]
plt.title('A Graph of Square of Values against Values', fontsize=15, color='orangered')
plt.xlabel('Values', fontsize=12.5, color='blue')
plt.ylabel('Square of Values', fontsize=12.5, color='green')


# plt.scatter(y_values, x_values)
plt.plot(y_values, x_values)
plt.show()