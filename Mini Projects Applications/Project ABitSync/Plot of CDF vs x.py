import matplotlib.pyplot as plt

x = [0,1,2,4]
P = [0.1,0.3,0.4,0.2]
x_plot = [-1,0,1,2,3,4,5]
CDF_plot = [0,0.1,0.4,0.8,0.8,1.0,1.0]
plt.figure(figsize = (10,5))
plt.step(x_plot,CDF_plot, where = 'post', label = 'CDF', color = 'red')
plt.scatter(x, [0.1, 0.4, 0.8, 1.0], color='blue', zorder=5, label='CDF jumps')
plt.title('CDF vs x')
plt.xlabel('x')
plt.ylabel('F(x)')
plt.xticks(range(-1, 6))
plt.yticks([0, 0.1, 0.4, 0.8, 1.0])
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()

plt.show()