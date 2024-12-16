import matplotlib.pyplot as plt
import numpy as np
import os

# Define the working directory
working_dir = r'C:\Users\veron\OneDrive\0-Writing-articles\GITHUB\public-python-code\2024-article-Moxa-in-stage-IV-metastatic-NSCLC'
# Change the current working directory
os.chdir(working_dir)

# Print the current working directory
print("Current working directory:", os.getcwd())



# Data Sorted by Hazard Ratio (Descending Order)
characteristics = [
    'TNM Stage 4B',
    'Sex: Males',
    'Radiotherapy: Yes',
    'Number of Chemocycles: > 3',
    'Moxa: 1\u20144 times',
    'TKI-TT: Any',
    'Moxa: > 4 times'
]

hazard_ratios = [
    1.43,  # TNM Stage 4B
    1.36,  # Sex: Males
    0.91,  # Radiotherapy: Yes
    0.85,  # Number of Chemocycles: 4–6
    0.80,  # Moxibustion: 1–4 times
    0.79,  # TKI2 Targeted therapy: Any
    0.52   # Moxibustion: >4 times
]

ci_lower = [
    1.14,  # TNM Stage 4B
    1.09,  # Sex: Males
    0.72,  # Radiotherapy: Yes
    0.59,  # Number of Chemocycles: 4–6
    0.61,  # Moxibustion: 1–4 times
    0.63,  # TKI2 Targeted therapy: Any
    0.37   # Moxibustion: >4 times
]

ci_upper = [
    1.79,  # TNM Stage 4B
    1.69,  # Sex: Males
    1.15,  # Radiotherapy: Yes
    1.21,  # Number of Chemocycles: 4–6
    1.03,  # Moxibustion: 1–4 times
    0.99,  # TKI2 Targeted therapy: Any
    0.73   # Moxibustion: >4 times
]


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
plt.savefig('hazard_ratio_plot6.png', format='png')
plt.savefig('hazard_ratio_plot6.svg', format='svg')
plt.savefig('hazard_ratio_plot6.tiff', format='tiff')  # Save as TIFF

 
# Show plot
plt.gca().invert_yaxis()  # Invert y-axis to have the first characteristic on top
plt.show()