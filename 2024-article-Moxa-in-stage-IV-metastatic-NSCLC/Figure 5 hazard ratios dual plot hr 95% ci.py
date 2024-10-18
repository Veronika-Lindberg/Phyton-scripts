import matplotlib.pyplot as plt
import numpy as np

def create_forest_plot(ax, data, color, title):
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
        ax.text(-0.1, y, f"{label} (n={n})", ha='right', va='center', fontsize=12, color='black')
        ax.text(1.05, y, f"{hr:.2f} ({ci_lower:.2f}-{ci_upper:.2f})", ha='left', va='center', fontsize=12, color='black')
    
    # Set up the plot
    ax.set_ylim(0.5, len(data) + 0.5)
    ax.set_xlim(0, 1.1)
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_xlabel('Hazard Ratio (95% CI)', fontsize=12, color='black')
    
    # Remove y-axis labels, ticks, and spine
    ax.set_yticks([])  # Remove y-ticks
    ax.spines['left'].set_visible(False)  # Hide the left spine (y-axis line)
    
    # Set all text to black
    ax.set_title(title, fontsize=12, color='black')
    
    # Add grid lines, but no vertical line at x=0
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    ax.axvline(x=1, color='gray', linestyle='--')
    
    # Add "Reference (HR=1)" text
    ax.text(1.05, len(data) + 0.5, 'Reference (HR=1)', ha='left', va='top', fontsize=12, color='black')

# Data for the plots
full_dataset = [
    ("PCB+oral-CHM only", 81, 1.00, 1.00, 1.00),
    ("+1-4 Moxa", 151, 0.68, 0.49, 0.94),
    ("+ TKI-TT", 36, 0.56, 0.36, 0.87),
    ("+ TKI-TT + 1-4 Moxa", 88, 0.63, 0.44, 0.90),
    ("+ >4 Moxa", 27, 0.40, 0.24, 0.65),
    ("+ TKI-TT + > 4 Moxa", 29, 0.45, 0.29, 0.72)
]

matched_dataset = [
    ("PCB+oral-CHM only", 80, 1.00, 1.00, 1.00),
    ("+1-4 Moxa", 63, 0.64, 0.43, 0.94),
    ("+ TKI-TT", 35, 0.56, 0.36, 0.87),
    ("+ TKI-TT + 1-4 Moxa", 33, 0.53, 0.34, 0.83),
    ("+ >4 Moxa", 12, 0.34, 0.18, 0.63),
    ("+ TKI-TT + > 4 Moxa", 7, 0.29, 0.15, 0.59)
]

# Create the plot with wider dimensions suitable for PowerPoint slide
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)  # Wider figure for PowerPoint

create_forest_plot(ax1, full_dataset, 'blue', 'Full dataset (n=412)')
create_forest_plot(ax2, matched_dataset, 'red', 'Propensity score matched dataset (n=230)')
# Save plot as an image file
plt.savefig('fig5.png', format='png')
plt.savefig('fig5.svg', format='svg')

plt.tight_layout()
plt.show()
