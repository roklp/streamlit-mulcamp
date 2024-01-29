# -*- coding:utf-8 -*-
import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

@st.cache_data
def cal_sales_revenue(price, total_sales):
    revenue = price * total_sales
    return revenue

@st.cache_data
def load_data():
    df = sns.load_dataset('iris')
    return df

def plot_matplotlib(df):
    st.title('Scatter Plot with Matplotlib')
    fig, ax = plt.subplots()
    ax.scatter(df['sepal_length'], df['sepal_width'])
    st.pyplot(fig)

def plot_seaborn(df):
    st.title('Scatter Plot with Seaborn')
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='sepal_length', y='sepal_width')
    st.pyplot(fig)

def plot_plotly(df):
    st.title('Scatter Plot with Plotly')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=df['sepal_length'], y=df['sepal_width'], mode='markers')
    )
    fig.update_layout(xaxis_title='sepal_length', yaxis_title='sepal_width')
    st.plotly_chart(fig)

def main():
    st.title("Button Widget")
    price = st.slider("단가:", 100, 10000, value=5000)
    total_sales = st.slider("전체 판매 갯수:", 1, 1000, value=500)

    st.write(price, total_sales)

    if st.button("매출액 계산"):
        revenue = cal_sales_revenue(price, total_sales)
        st.write(revenue)

    st.title("Check Box Control")
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    show_plot = st.checkbox("시각화 보여주기")
    st.write(show_plot)

    if show_plot:
        fig, ax = plt.subplots()
        ax.plot(x, y)
        st.pyplot(fig)

    st.title("라이브러리 선택")
    iris = load_data()
    st.dataframe(iris)

    plot_type = st.radio(
        "뭔 산점도 보고싶냐",
        ("Matplotlib", "Seaborn", "Plotly")
    )

    if plot_type == "Matplotlib":
        plot_matplotlib(iris)
    elif plot_type == "Seaborn":
        plot_seaborn(iris)
    elif plot_type == "Plotly":
        plot_plotly(iris)

   

if __name__ == "__main__":
    main()
