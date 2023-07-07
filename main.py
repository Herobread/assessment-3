import numpy as np
import matplotlib.pyplot as plt

# Load data from the CSV file
data = np.loadtxt('data/guinea.csv', delimiter=',')

# Extract data columns using meaningful variable names
index = data[:, 0]
tooth_length = data[:, 1]
supplement_type = data[:, 2]
dose = data[:, 3]

# Separate data for
# vitamin C    - type 0, vc
# orange juice - type 1, oj
vc_indices = np.where(supplement_type == 0)
oj_indices = np.where(supplement_type == 1)

vc_dose = dose[vc_indices]
vc_length = tooth_length[vc_indices]
oj_dose = dose[oj_indices]
oj_length = tooth_length[oj_indices]

# Create a scatter plot
plt.scatter(vc_dose, vc_length, c='blue', label='Vitamin Capsule')
plt.scatter(oj_dose, oj_length, c='orange', label='Orange Juice')

# Set labels and title
plt.xlabel('Dose (mg/day)')
plt.ylabel('Tooth Length (mm)')
plt.title('Dose vs Tooth Length for Different Supplement Types')

# Add legend, grid, and display the plot
plt.legend()
plt.grid()
plt.show()
