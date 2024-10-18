import matplotlib.pyplot as plt
import numpy as np
import os

# Define the working directory
working_dir = r'C:\Users\veron\OneDrive\0-Writing-articles\GITHUB\public-python-code\2024-article-Moxa-in-stage-IV-metastatic-NSCLC'
# Change the current working directory
os.chdir(working_dir)

def create_forest_plot(ax, data, color, title):
    # Reverse the order of the covariates
    data = data[::-1]
    
    # Create y positions with reduced vertical space between categories
    y_positions = np.linspace(len(data), 1, len(data))  # Decreases the vertical space
    
    for i, (label, n, hr, ci_lower, ci_upper) in enumerate(data):
        y = y_positions[i]
        
        # Plot confidence interval
        ax.plot([ci_lower, ci_upper], [y, y], color=color, linewidth=2)
        
        # Plot hazard ratio point: square for HR=1.0, circle for others
        if hr == 1.0:
            ax.scatter(hr, y, color=color, s=50, marker='s')  # Square for HR=1.0
        else:
            ax.scatter(hr, y, color=color, s=50, marker='o')  # Circle for others
        
        # Move category text outside the graph, on the left
        ax.text(-0.15, y, f"{label} (n={n})", ha='right', va='center', fontsize=12, color='black', transform=ax.get_yaxis_transform(), bbox=dict(facecolor='white', edgecolor='none', pad=0))
        ax.text(1.05, y, f"{hr:.2f} ({ci_lower:.2f}-{ci_upper:.2f})", ha='left', va='center', fontsize=12, color='black', transform=ax.get_yaxis_transform(), bbox=dict(facecolor='white', edgecolor='none', pad=0))
    
    # Set up the plot
    ax.set_ylim(0.5, len(data) + 0.5)
    ax.set_xlim(0.1, 1.0)  # Start x-axis at 0.1 and end at 1.0
    ax.set_xticks([0.2, 0.4, 0.6, 0.8, 1.0])  # Add x-tick numbers
    ax.set_xlabel('Hazard Ratio (95% CI)', fontsize=12, color='black')
    
    # Remove y-axis labels, ticks, and spine
    ax.set_yticks([])  # Remove y-ticks
    ax.spines['left'].set_visible(False)  # Hide the left spine (y-axis line)
    ax.spines['top'].set_visible(False)  # Hide the top spine (upper line)
    ax.spines['right'].set_visible(False)  # Hide the right spine (vertical line at end of plot)
    
    # Set all text to black
    ax.set_title(title, fontsize=12, color='black')
    
    # Add grid lines, but no vertical line at x=0 or x=1.1
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    ax.axvline(x=1, color='gray', linestyle='--')  # Reference line at HR=1
    
    # Add "Reference (HR=1)" text
    ax.text(1.05, len(data) + 0.5, 'Reference (HR=1)', ha='left', va='top', fontsize=12, color='black')

# Data for the plots
full_dataset = [
    ("+ Moxa 1\u20144 times", 151, 0.68, 0.49, 0.94),
    ("+ TKI-TT", 36, 0.56, 0.36, 0.87),
    ("+ TKI-TT + Moxa 1\u20144 times", 88, 0.63, 0.44, 0.90),
    ("+ Moxa >4 times", 27, 0.40, 0.24, 0.65),
    ("+ TKI-TT + Moxa >4 times", 29, 0.45, 0.29, 0.72),
    ("PCB+oral-CHM only", 81, 1.00, 1.00, 1.00)
]

matched_dataset = [
    ("+ Moxa 1\u20144 times", 63, 0.64, 0.43, 0.94),
    ("+ TKI-TT", 35, 0.56, 0.36, 0.87),
    ("+ TKI-TT + Moxa 1\u20144 times", 33, 0.53, 0.34, 0.83),
    ("+ Moxa >4 times", 12, 0.34, 0.18, 0.63),
    ("+ TKI-TT + Moxa >4 times", 7, 0.29, 0.15, 0.59),
    ("PCB+oral-CHM only", 80, 1.00, 1.00, 1.00),
]

# Create the plot with wider dimensions suitable for PowerPoint slide
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)  # Wider figure for PowerPoint

create_forest_plot(ax1, full_dataset, 'blue', 'Full dataset (n=412)')
create_forest_plot(ax2, matched_dataset, 'red', 'Propensity score matched dataset (n=230)')

# Save plot as an image file
plt.savefig('fig5-3.png', format='png')
plt.savefig('fig5-3.svg', format='svg')

plt.tight_layout()
plt.show()