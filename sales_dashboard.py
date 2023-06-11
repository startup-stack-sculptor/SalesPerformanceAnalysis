import pandas as pd
import plotly.express as px
import streamlit as st


import calendar

# Get the list of month names
months = calendar.month_name[1:]



# Read the sales data from a CSV file
sales_data = pd.read_csv("data/Sales_April_2019.csv")
df = pd.DataFrame(sales_data)
df["Price Each"] = pd.to_numeric(df["Price Each"], errors='coerce')
df["Quantity Ordered"] = pd.to_numeric(df["Quantity Ordered"], errors='coerce')
df['City'] = df['Purchase Address'].str.split(',').str[1].str.strip()

# Extract the relevant columns

# Create a line plot for the revenue

# Create a bar chart for the units sold


def main():
    # Page title
    st.title('Sales Performance Analysis')
    st.write('Data Split up by months')

    # Sidebar
    st.sidebar.header("Please Filter here:")

    cities = st.sidebar.multiselect(
        "select the cities",
        options=df['City'].unique(),
        default=[]
    )
    price = st.sidebar.multiselect(
        "Select the product price",
        options=df["Price Each"].unique(),
        default=[]
    )

    quantity = st.sidebar.multiselect(
        "Select the quantity",
        options=df["Quantity Ordered"].unique(),
        default=[]
    )

    product = st.sidebar.multiselect(
        "Select the product",
        options=df["Product"].unique(),
        default=[]
    )


    # File Upload

    # Total sales by month
    df_selection = df.query(
        "City == @cities"
    )
    total_sales = df_selection["Quantity Ordered"].astype(int).sum()
    left_column, middle_column, right_column = st.columns(3)

    with left_column:
        st.subheader("Total sales:")
        st.subheader(f"Qty {total_sales}")

    with middle_column:
        st.subheader("Average rating")

    with right_column:
        st.subheader("Average sales per transaction")

    # Sales by region
    sales_no_by_city = df_selection.groupby(by=['City']).sum()[["Quantity Ordered"]].sort_values(by="Quantity Ordered")

    fig_product_sales = px.bar(
        sales_no_by_city,
        x="Quantity Ordered",
        y=sales_no_by_city.index,
        orientation="h",
        title="<b>Sales by city</b>",
        color_discrete_sequence=['#0083BB'] * len(sales_no_by_city),
        template="plotly_white"
    )

    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig_product_sales, use_container_width=True)

    # Sales by hour (BAR CHART)

    # Sales by Product line (Bar Chart)

    # Top KPI

    

if __name__ == '__main__':
    main()

