
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = "/content/eegIDRecord_4new.csv" # The path to your uploaded CSV file

# Check if the file exists
if not os.path.exists(file_path):
    print(f"Error: The file '{file_path}' was not found. Please ensure the file is uploaded to the correct path.")
else:
    try:
        df = pd.read_csv(file_path)

        x_column = 'timestampMs'
        y_columns_to_plot = ['attention', 'meditation', 'blinkStrength', 'delta', 'theta']

        # Define a list of colors for each wave type
        # You can use color names (e.g., 'blue', 'green', 'red'), hex codes (e.g., '#FF5733'),
        # or RGB tuples (e.g., (0.1, 0.2, 0.5))
        colors = ['blue', 'green', 'red', 'purple', 'orange'] # Example colors

        num_plots = len(y_columns_to_plot)
        fig, axes = plt.subplots(nrows=num_plots, ncols=1, figsize=(15, 4 * num_plots), sharex=True)

        if num_plots == 1:
            axes = [axes]

        for i, col in enumerate(y_columns_to_plot):
            if col in df.columns:
                #df[col] = pd.to_numeric(df[col], errors='coerce')
                # Use the color from the 'colors' list based on the index 'i'
                axes[i].plot(df[x_column], df[col], label=col, linewidth=1.5, color=colors[i % len(colors)])
                axes[i].set_ylabel(col.replace('Strength', ' Strength').title())
                axes[i].set_title(f'{col.replace("Strength", " Strength").title()} Wave')
                axes[i].grid(True)
                axes[i].legend(loc='upper right')
            else:
                print(f"Warning: Column '{col}' not found in the CSV file. Skipping this subplot.")

        axes[-1].set_xlabel('Time (timestampMs)')

        plt.suptitle('Separate Wave Graphs of EEG Data Over Time', y=1.02, fontsize=16)
        plt.tight_layout(rect=[0, 0.03, 1, 0.98])
        plt.show()

    except KeyError as e:
        print(f"Error: A critical column was not found. Please check column names in your CSV. {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
     


  colors = ['blue', 'green', 'red', 'purple', 'orange']
 print(colors)
     


import os
os.getcwd()
     


import matplotlib.pyplot as plt

x_column = 'timestampMs'
y_columns_to_compare = ['attention', 'meditation', 'blinkStrength']

plt.figure(figsize=(15, 6))

for col in y_columns_to_compare:
    if col in df.columns:
        # Ensure the column is numeric
        df[col] = pd.to_numeric(df[col], errors='coerce')
        plt.plot(df[x_column], df[col], label=col, linewidth=1.5)
    else:
        print(f"Warning: Column '{col}' not found in the CSV file. Skipping this plot.")

plt.xlabel('Time (timestampMs)')
plt.ylabel('Value')
plt.title('Comparison of Attention, Meditation, and Blink Strength Over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
#plt.show()