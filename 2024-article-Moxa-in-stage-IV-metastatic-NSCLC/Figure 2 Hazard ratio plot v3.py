import matplotlib.pyplot as plt
import numpy as np
import os

# Define the working directory
working_dir = r'C:\Users\veron\OneDrive\0-Writing-articles\GITHUB\public-python-code\2024-article-Moxa-in-stage-IV-metastatic-NSCLC'
# Change the current working directory
os.chdir(working_dir)

# Print the current working directory
print("Current working directory:", os.getcwd())

# Data
characteristics = [
    'TNM Stage 4B',
    'Sex: Male',
    'Radiotherapy',
    'TKI-TT',
    'CPM',
    'Moxa 1\u20144 times',
    'Chemo Cycles >3',
    'Moxa >4 times'
]
hazard_ratios = [1.49, 1.39, 0.88, 0.81, 0.75, 0.74, 0.67, 0.55]
ci_lower = [1.16, 1.08, 0.68,0.61,  0.59, 0.58, 0.44, 0.36]
ci_upper = [1.91, 1.78, 1.13,1.06,  0.96, 0.95, 1.01, 0.82]

# Convert data to numpy arrays for easier manipulation
y_pos = np.arange(len(characteristics))

# Set default font properties
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# Plot
plt.figure(figsize=(10, 6))
plt.errorbar(hazard_ratios, y_pos, xerr=[np.array(hazard_ratios) - np.array(ci_lower), np.array(ci_upper) - np.array(hazard_ratios)], fmt='ko', ecolor='black')
plt.yticks(y_pos, characteristics)
plt.axvline(x=1, color='grey', linestyle='--')

# Expand x-axis limits
plt.xlim(0, 2.5)

# Add grid at 0.2 intervals on x-axis in grey
plt.grid(axis='x', color='grey', linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0.2, 1.8, 0.2))

# Ensure the x-axis spine is visible and set its color to black
plt.gca().spines['bottom'].set_visible(True)
plt.gca().spines['bottom'].set_color('black')

# Remove the spines at x=0 and the last x-tick
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Labels and title
plt.xlabel('Hazard Ratio (95% CI)')
# plt.title('Hazard Ratios for Various Characteristics in Stage IV Metastatic NSCLC')
plt.title('')

# Adjust layout to ensure text fits within the plot area
plt.tight_layout()
plt.subplots_adjust(left=0.3)  # Adjust left margin to provide more space for y-axis labels

# Add HR and CI annotations
for i in range(len(characteristics)):
    hr_text = f'HR {hazard_ratios[i]:.2f} ({ci_lower[i]:.2f}-{ci_upper[i]:.2f})'
    plt.text(2.0, i, hr_text, verticalalignment='center', fontsize=10)

# Remove y-axis ticks and lines
plt.tick_params(axis='y', which='both', left=False)

# Save plot as an image file
plt.savefig('hazard_ratio_plot3.png', format='png')
plt.savefig('hazard_ratio_plot3.svg', format='svg')

 
# Show plot
plt.gca().invert_yaxis()  # Invert y-axis to have the first characteristic on top
plt.show()