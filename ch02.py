import streamlit as st
import seaborn as sns
import pandas as pd

@st.cache_data
def load_data():
    df = sns.load_dataset("tips") 
    return df

def main():
    st.write(st.__version__)
    st.write(sns.__version__)
    st.write(pd.__version__)

    tips = load_data()  
    st.dataframe(tips, use_container_width=True)

    st.write("-" * 50)
    st.title("st.metric()")
    tip_max = tips['tip'].max()  # 최대값
    tip_min = tips['tip'].min()  # 최소값

    st.metric(label="팁 최고금액", value=tip_max, delta=tip_max - tip_min)
    st.metric(label="팁 최소금액", value=tip_min, delta=tip_min - tip_max)

if __name__ == "__main__":
    main()

st.title("케이티 배정대~")
