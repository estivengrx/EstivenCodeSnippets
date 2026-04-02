# Code snippet to set a scientific style for plotting in matplotlib, using the SciencePlots package.
# First do: pip install SciencePlots (REQUIRES LATEX INSTALLED), then:
import scienceplots
import matplotlib.pyplot as plt

plt.style.use(['science', 'ieee'])

# Create data and plot
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25] 
plt.plot(x, y)

plt.title(r'Scientific Plot $L = \sum_i \frac{1}{2} m_i \dot{r}_i^2 -\sum_i q_i \phi(x_i) + \sum_i q_i \mathbf{A}(x_i) \cdot \dot{\mathbf{r}}_i$')

plt.xlabel('X-axis $\\frac{1}{2}$') # works both with r'latex expression' or with \\ in the string, but the first one is more readable.
plt.ylabel('Y-axis')
plt.show()
# To see further of this library, check the documentation: https://github.com/garrettj403/SciencePlots