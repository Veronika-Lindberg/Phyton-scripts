import matplotlib.pyplot as plt
import numpy as np
import textwrap
import os

# Define the working directory
working_dir = r'C:\Users\veron\OneDrive\0-Writing-articles\GITHUB\public-python-code\2024-article-Patent-CHM-in-stage-IV-metastatic-NSCLC'
# Change the current working directory
os.chdir(working_dir)

# Print the current working directory
print("Current working directory:", os.getcwd())



# Data Sorted by Hazard Ratio (Descending Order)
characteristics = [
    'TNM Stage: 4B (vs 4A)',
        'Sex: Males (vs Females)',
        'Radiotherapy: Yes (vs No)',
        'Number of Chemocycles: 4-6 (vs < 4)',
        'TKI Targeted therapy: Any (vs None)',
       # 'Moxibustion: ≥ 1 times (vs None)',
       # 'CPM: 1\u20144 Oral treatments or Any Intravenous CPM (vs No CPM)',
       # 'CPM: >4 Oral treatements alone, or Any Oral treatments combined with Any Intravenous CPM (vs No CPM)'
       'CPM: Any Oral or Intravenous treatements (vs No CPM)',
       'CPM: Moderate (vs No CPM)',
       'CPM: Intensive (vs No CPM)'
]

# Wrap the text for each characteristic
wrapped_characteristics = [textwrap.fill(char, width=35) for char in characteristics]


hazard_ratios = [
    1.43,
        1.36,
        0.91,
        0.85,
        0.79,
      #  0.72,
        0.65,
        0.84,
        0.54
]

ci_lower = [
    1.14,
        1.09,
        0.72,
        0.59,
        0.63,
      #  0.56,
        0.51,
        0.63,
        0.42
]

ci_upper = [
     1.79,
        1.69,
        1.15,
        1.21,
        0.99,
       # 0.92,
        0.82,
        1.10,
        0.71
]


# Convert data to numpy arrays for easier manipulation
y_pos = np.arange(len(characteristics))

# Set default font properties
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

# Plot
plt.figure(figsize=(10, 6))
plt.errorbar(hazard_ratios, y_pos, xerr=[np.array(hazard_ratios) - np.array(ci_lower), np.array(ci_upper) - np.array(hazard_ratios)], fmt='ko', ecolor='black')
plt.yticks(y_pos, wrapped_characteristics)
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
plt.savefig('Figure 7.png', format='png')
plt.savefig('Figure 7.jpg', format='jpg')
plt.savefig('Figure 7.svg', format='svg')
plt.savefig('Figure 7.tiff', format='tiff')  # Save as TIFF

 
# Show plot
plt.gca().invert_yaxis()  # Invert y-axis to have the first characteristic on top
plt.show()