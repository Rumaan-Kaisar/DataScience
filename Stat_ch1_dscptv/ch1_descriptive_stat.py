
# ----------------------  Bar chart  ----------------------

import matplotlib.pyplot as plt

# Data
brands = ["Audi", "BMW", "Mercedes", "Total"]
sales = [124, 98, 113, 335]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]  # Blue, Orange, Green, Red

# Create the bar chart
plt.figure(figsize=(8, 6))
bars = plt.bar(brands, sales, color=colors, edgecolor="black", linewidth=1.2)

# Add labels and title
plt.xlabel("Car Brands", fontsize=12)
plt.ylabel("Units Sold", fontsize=12)
plt.title("Car Brand Sales", fontsize=16)

# Display values on top of bars
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5, 
             str(bar.get_height()), ha="center", va="bottom", fontsize=12, fontweight="bold")

# show grids
plt.grid(True, linestyle="--", alpha=0.7)  # Enables grid with dashed lines and transparency
plt.ylim(0, 360)  # Adjust the Y-axis from 0 to 350


# Modify axis colors & opacity
# ax = plt.gca()
# ax.spines["bottom"].set_color("red")     # X-axis in red
# ax.spines["left"].set_color("blue")      # Y-axis in blue
# ax.spines["top"].set_color("gray")       # Optional: Gray top border
# ax.spines["right"].set_color("gray")     # Optional: Gray right border
# ax.spines["bottom"].set_alpha(0.5)       # X-axis opacity (50%)
# ax.spines["left"].set_alpha(0.7)         # Y-axis opacity (70%)

# Save as SVG for Illustrator
plt.savefig("car_sales.svg", format="svg", dpi=300)

# Show the chart
plt.show()



# ----------------------  Pie chart  ----------------------
import matplotlib.pyplot as plt

# Data
brands = ["Audi", "BMW", "Mercedes"]
sales = [124, 98, 113]
colors = ["#4E79A7", "#A0CBE8", "#F28E2B"]  # Muted, modern colors

# Create pie chart
plt.figure(figsize=(6, 6))
plt.pie(
    sales,
    labels=brands,
    colors=colors,
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 1},
    textprops={"fontsize": 12, "color": "#333"},
    autopct="%1.1f%%"
)

# Minimalist styling
plt.title("Car Brand Market Share", fontsize=14, color="#333", pad=20)
plt.tight_layout()
plt.show()



# ----------------------  Pareto Diagram  ----------------------
import matplotlib.pyplot as plt
import numpy as np

# Data
brands = ["Audi", "BMW", "Mercedes"]
sales = [124, 98, 113]

# Sort data by sales descending
sorted_indices = np.argsort(sales)[::-1]
brands_sorted = [brands[i] for i in sorted_indices]
sales_sorted = [sales[i] for i in sorted_indices]

# Cumulative percentage
cumulative = np.cumsum(sales_sorted)
cumulative_percent = 100 * cumulative / sum(sales_sorted)

# Create figure and axis
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart (Pareto bars)
bars = ax1.bar(brands_sorted, sales_sorted, color="#4E79A7", edgecolor='white', width=0.6)
ax1.set_ylabel("Units Sold", fontsize=12)
ax1.set_xlabel("Car Brands", fontsize=12)
ax1.set_title("Pareto Diagram - Car Sales", fontsize=14, color="#333", pad=20)
ax1.tick_params(axis='y', labelcolor="#4E79A7")

# Annotate bars with ranks
for i, bar in enumerate(bars):
    label = f"Top {i+1}"
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2, label,
             ha='center', fontsize=10, color="#333")

# Line chart (Cumulative %)
ax2 = ax1.twinx()
ax2.plot(brands_sorted, cumulative_percent, color="#F28E2B", marker="o", linewidth=2)
ax2.set_ylabel("Cumulative Percentage", fontsize=12, color="#F28E2B")
ax2.tick_params(axis='y', labelcolor="#F28E2B")

# Horizontal line to highlight "vital few" (e.g., 80% line)
ax2.axhline(80, color="gray", linestyle="--", linewidth=1)
ax2.text(len(brands_sorted)-1, 81, "80% Threshold", ha="right", va="bottom", fontsize=10, color="gray")

# Minimalist styling
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)


# Add Y-axis grid to bar chart axis
ax1.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)
ax2.grid(True, which='major', axis='y', linestyle='--', linewidth=0.5, color='#F28E2B', alpha=0.7)


plt.tight_layout()
plt.show()



# ----------------------  Histogram  ----------------------

import matplotlib.pyplot as plt

# Data
dataset = [1, 9, 22, 24, 32, 33, 41, 44, 57, 66, 70, 
           73, 75, 76, 79, 82, 87, 89, 95, 100]

# Define equal-width bins (1–20, 21–40, ..., 81–100)
bins = [1, 20, 40, 60, 80, 100]

# Plot
plt.figure(figsize=(8, 5))
plt.hist(dataset, bins=bins, color="#00c4b0", edgecolor="white", linewidth=1.2, rwidth=1.0)

# Labels and title
plt.xlabel("Value Ranges", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Histogram of Dataset", fontsize=14, color="#007fff", pad=15)

# Gridlines
plt.grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.7, color="#6d9bc3")

# Minimalist styling
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()


# NOTE: if bin widths are equal, setting "density=True" is enough to make it a relative frequency-style plot
plt.hist(dataset, bins=bins, density=True, color="#ffa600", edgecolor="white", linewidth=1.2, rwidth=1.0)



# ----------------------  Histogram: Absolute vs Relative Frequency  ----------------------
import matplotlib.pyplot as plt

# Data
dataset = [1, 9, 22, 24, 32, 33, 41, 44, 57, 66, 70, 
           73, 75, 76, 79, 82, 87, 89, 95, 100]

# Define bins: 1–20, 21–40, ..., 81–100 (extend to 101 to include 100)
bins = [1, 20, 40, 60, 80, 100]

# Create subplots (NO sharey=True)
fig, axs = plt.subplots(1, 2, figsize=(12, 5))  # Removed sharey=True
# sharey=True causes problem
# fig, axs = plt.subplots(1, 2, figsize=(12, 5), sharey=True)   

# --- Absolute Frequency Histogram ---
axs[0].hist(dataset, bins=bins, color="#00c4b0", edgecolor="white", linewidth=1.2, rwidth=1.0)
axs[0].set_title("Absolute Frequency", fontsize=13, color="#007fff", pad=12)
axs[0].set_xlabel("Value Ranges", fontsize=11)
axs[0].set_ylabel("Count", fontsize=11)
axs[0].grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.7, color="#6d9bc3")
for spine in axs[0].spines.values():
    spine.set_visible(False)

# --- Relative Frequency Histogram ---
axs[1].hist(dataset, bins=bins, weights=[1./len(dataset)]*len(dataset), 
            color="#ffa600", edgecolor="white", linewidth=1.2, rwidth=1.0)
axs[1].set_title("Relative Frequency", fontsize=13, color="#ff7c00", pad=12)
axs[1].set_xlabel("Value Ranges", fontsize=11)
axs[1].set_ylabel("Proportion", fontsize=11)
axs[1].grid(axis='y', linestyle='--', linewidth=0.6, alpha=0.7, color="#c98f3b")
for spine in axs[1].spines.values():
    spine.set_visible(False)

plt.suptitle("Histogram Comparison: Absolute vs Relative Frequency", fontsize=15, color="#333", y=1.05)
plt.tight_layout()
plt.show()



# ----------------------  Cross table and side by side bar chart  ----------------------

# dataFrame making
import pandas as pd

# Original data
data = {
    "Type of investment": ["Stocks", "Bonds", "Real Estate"],
    "Investor A": [96, 181, 88],
    "Investor B": [185, 3, 152],
    "Investor C": [39, 29, 142]
}

# Create DataFrame
df = pd.DataFrame(data)

# Set index to make it look like a cross-table
cross_table = df.set_index("Type of investment")

# Add row totals
cross_table["Total"] = cross_table.sum(axis=1)

# Add column totals (including the new "Total" column)
cross_table.loc["Total"] = cross_table.sum()

print(cross_table)


# Cross table (side by side investment comparison)

import matplotlib.pyplot as plt
import numpy as np

# Data from cross table
investments = data["Type of investment"]
investor_a = data["Investor A"]
investor_b = data["Investor B"]
investor_c = data["Investor C"]

# Bar width and x positions
bar_width = 0.25
x = np.arange(len(investments))

# Create plot
plt.figure(figsize=(9, 5))
plt.bar(x - bar_width, investor_a, width=bar_width, label="Investor A", color="#1f77b4")
plt.bar(x, investor_b, width=bar_width, label="Investor B", color="#ff7f0e")
plt.bar(x + bar_width, investor_c, width=bar_width, label="Investor C", color="#2ca02c")

# Labels and styling
plt.xlabel("Type of Investment", fontsize=12)
plt.ylabel("Investment Amount", fontsize=12)
plt.title("Side-by-Side Investment Comparison", fontsize=14, color="#333")
plt.xticks(x, investments, fontsize=11)
plt.yticks(fontsize=10)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Minimalist styling
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()



# cross table (investments per investor)

import matplotlib.pyplot as plt
import numpy as np

# Data from cross table
investments = data["Type of investment"]
investor_a = data["Investor A"]
investor_b = data["Investor B"]
investor_c = data["Investor C"]

# Transpose structure: group by investor
x = np.arange(len(["Investor A", "Investor B", "Investor C"]))  # 3 investors
bar_width = 0.25

# Stack asset allocations per investor
stocks = [investor_a[0], investor_b[0], investor_c[0]]
bonds = [investor_a[1], investor_b[1], investor_c[1]]
real_estate = [investor_a[2], investor_b[2], investor_c[2]]

# Plot
plt.figure(figsize=(9, 5))
plt.bar(x - bar_width, stocks, width=bar_width, label="Stocks", color="#00c4b0")
plt.bar(x, bonds, width=bar_width, label="Bonds", color="#ff2052")
plt.bar(x + bar_width, real_estate, width=bar_width, label="Real Estate", color="#007fff")

# Labels and styling
plt.xlabel("Investor", fontsize=12)
plt.ylabel("Investment Amount", fontsize=12)
plt.title("Investment Allocation per Investor", fontsize=14, color="#333")
plt.xticks(x, ["Investor A", "Investor B", "Investor C"], fontsize=11)
plt.yticks(fontsize=10)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Minimalist frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()
plt.show()




# ----------------------  Scatter plot for "SAT scores".  ----------------------

# Data conversion to a csv file.
import pandas as pd

# Step 1: Define the data
# (Student ID, Reading, Writing)
data = [(1, 273,216),
        # data from the table, in tuple form like this
        (104, 549,521)]

# Step 2: Create DataFrame
df = pd.DataFrame(data, columns=["Student ID", "Reading", "Writing"])

# Step 3: Save to CSV
df.to_csv("SAT_scores.csv", index=False)

# Step 4: Load back from CSV
loaded_df = pd.read_csv("SAT_scores.csv")

print(loaded_df)


# Scatter plot (styled plot):
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("ch1_data_SAT_scores.csv")

# Modern font settings
plt.rcParams["font.family"] = "DejaVu Sans"

# Create the scatterplot
plt.figure(figsize=(8, 5))
plt.scatter(df["Reading"], df["Writing"], 
            color="#89cff0", edgecolors='#318ce7', 
            s=45, alpha=0.8)

# Title and axis labels
plt.title("Reading vs Writing Scores", fontsize=15, color="#54626f", pad=15)
plt.xlabel("Reading Score", fontsize=12, color="#87a96b")
plt.ylabel("Writing Score", fontsize=12, color="#87a96b")

# Modern tick colors and font size
plt.xticks(color="#54626f", fontsize=10)
plt.yticks(color="#54626f", fontsize=10)

# Grid and minimalist style
plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.6, color="#72a0c1")
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.tight_layout()

# Save as SVG
# plt.savefig("sat_scores_scatter_modern.svg", format="svg")

# Optional: show the plot
plt.show()




