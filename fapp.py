import streamlit as st
import plotly.express as px

st.set_page_config(
    layout="wide",
    page_title="simple dashboard"
)
df = px.data.tips()
#sidebar
x = st.sidebar.checkbox("showdata", False, key = 1)
day = st.sidebar.selectbox('select day', df['day'].unique())
time = st.sidebar.selectbox('select meal time', df['time'].unique())
size = st.sidebar.radio("select how many dishes", sorted(df['size'].unique()), 3, horizontal = True)
if x:
    st.header('dataset sample')
    st.dataframe(df.head(8))
    
#page content
col1, col2, col3 = st.columns([5,2,5])

with col1:
    new_df1 = df[df['day'] == day]
    fig = px.histogram(new_df1, x = 'total_bill', color = 'sex', title= f'total bill for {day}'.title(),width = 700)
    
    st.plotly_chart(fig, use_container_width = True)
    fig= px.pie(new_df1, names = 'time', color = 'sex', title = f'count of each meal time according to {size} dishes'.title()).update_traces(textinfo='value')
    st.plotly_chart(fig,use_container_width = True)
    
with col3:
    new_df2 = df[df['time']== time]
    fig = px.scatter(new_df2, x= 'total_bill', y = "tip", template = "presentation", size_max = 20, color="sex", title = f'correlation btww tot bill and tip on {time}') 
    fig = px.sunburst(df, path= ["day", "time", "size"], color='tip', title= f"counting over day, times and size over tips".title())
    st.plotly_chart(fig, use_container_width = True)
