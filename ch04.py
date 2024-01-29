import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px 
from plotly.subplots import make_subplots
import plotly

@st.cache_data
def load_data():
    df = sns.load_dataset('tips')
    return df

def main():
    st.title("NC Dions")
    
    tips = load_data()  
    

    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]
    
   
    fig, ax = plt.subplots(ncols=2, figsize=(10, 6), sharex=True, sharey=True)
    ax[0].scatter(x=m_tips['total_bill'], y=m_tips['tip'])
    ax[0].set_title('Male')
    ax[1].scatter(x=f_tips['total_bill'], y=f_tips['tip'])
    ax[1].set_title('Female')

    tips = load_data()  
    
    m_tips = tips.loc[tips['sex'] == 'Male', :]
    f_tips = tips.loc[tips['sex'] == 'Female', :]
     
    st.subheader("Plotly를 이용한 산점도")
    
    fig1 = px.scatter(m_tips, x='total_bill', y='tip', title='Male Tips')
    st.plotly_chart(fig1)
    
    fig2 = px.scatter(f_tips, x='total_bill', y='tip', title='Female Tips')
    st.plotly_chart(fig2)

    fig = make_subplots(rows = 1,
                        cols = 2,
                        subplot_titles=('Male', 'Female'),
                        shared_yaxes=True,
                        shared_xaxes=True,
                        x_title='Total Bill($)'
                        )
    fig.add_trace(go.Scatter(x = m_tips['total_bill'], y = m_tips['tip'], mode='markers'), row=1, col=1)
    fig.add_trace(go.Scatter(x = f_tips['total_bill'], y = f_tips['tip'], mode='markers'), row=1, col=2)
    fig.update_yaxes(title_text="Tip($)", row=1, col=1)
    fig.update_xaxes(range=[0, 60])
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
