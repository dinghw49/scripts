import numpy as np
import subprocess
import sys
# ... (previous code for extracting data)

import subprocess

# Run 'grep cc REPORT' and save the third column to a file named 'xxx'
subprocess.run(['grep', 'cc', 'REPORT'], stdout=open('xxx', 'w'))

# Run 'grep b_m REPORT' and save the second column to a file named 'fff'
subprocess.run(['grep', 'b_m', 'REPORT'], stdout=open('fff', 'w'))

# Combine the contents of 'xxx' and 'fff' side by side and save the result to 'grad.dat'
subprocess.run(['paste', 'xxx', 'fff'], stdout=open('grad.dat', 'w'))

# Remove the temporary files 'xxx' and 'fff'
subprocess.run(['rm', 'xxx'])
subprocess.run(['rm', 'fff'])


# Read input data and extract specific columns
with open('grad.dat', 'r') as file:
    lines = file.readlines()

# Process lines to extract columns 2 and 7
extracted_data = []
for line in lines:
    columns = line.split()
    if len(columns) >= 7:  # Ensure that the line has at least 7 columns
        data_point = f"{columns[2]}\t{columns[6]}"
        extracted_data.append(data_point)

# Save the extracted data to 'grad.dat'
with open('grad.dat', 'w') as file:
    file.write('\n'.join(extracted_data))


# Read the input filename from command line arguments
input_file = 'grad.dat'

# Open the input file for reading
with open(input_file, 'r') as f:
    r = []
    g = []

    # Read data from the file
    for line in f.readlines():
        line = line.split()
        # Process each line and append data to lists
        print(len(line))
        if len(line) == 2:
            r.append(float(line[0]))
            g.append(float(line[1]))

# Calculate and print the free energy values
tg = 0.0
with open('free_energy.dat', 'w') as output_file:
    output_file.write(f"{r[0]} {tg}\n")
    for i in range(1, len(r)):
        gg = 0.5 * (r[i] - r[i-1]) * (g[i] + g[i-1])
        tg += gg
        output_file.write(f"{r[i]} {tg}\n")

import matplotlib.pyplot as plt
import numpy as np

# Read data from 'free_energy.dat' file
data = np.loadtxt('free_energy.dat')

# Extract columns
r, tg = data[:, 0], data[:, 1]

# Plot the data
plt.plot(r, tg, label='Free Energy')
plt.xlabel('Collective variable (Ang)')
plt.ylabel('Free energy (eV)')
plt.legend()
plt.grid(True)
plt.title('Free Energy Profile')
plt.savefig('free_energy.jpg')
plt.show()
