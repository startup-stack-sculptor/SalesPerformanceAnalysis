import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


# Read the sales data from a CSV file
sales_data = pd.read_csv("data/Sales_April_2019.csv")
df = pd.DataFrame(sales_data)
columns = df.columns.tolist()
print(columns)

# Extract the relevant columns

# Create a line plot for the revenue

# Create a bar chart for the units sold


def main():
    # Page title
    st.title('Sales Performance Analysis')
    st.write('Data Split up by months')

    # File Upload

    # Total sales by month

    # Sales by region

    # Sales by hour (BAR CHART)

    # Sales by Product line (Bar Chart)

    # Top KPI

    

if __name__ == '__main__':
    main()

    
