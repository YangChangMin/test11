import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

a = st.number_input('a의 값을 입력하시오',value=2.0,step=1.0)
b = st.number_input('b의 값을 입력하시오',value=-1.0,step=1.0)
c = st.number_input('c의 값을 입력하시오',value=15.0,step=1.0)
d= st.number_input('d의 값을 입력하시오',value=2000.0,step=100.0)

c1 = st.sidebar.radio('선의 색을 선택하시오',['red','blue','orange','purple'])
s1 = st.sidebar.radio('선의 스타일을 선택하시오',['-','--','~'])
m1 = st. sidebar.radio('마커의 스타일을 선택하시오',['o','^','s','p'])


x = []
y1 = []
for i in range(-29,30,3):
    x.append(i)
    y1.append(a*i*i + b*i + c)

x = []
y2 = []
for i in range(-29, 30, 3):
    x.append(i)

    y2.append(d/i)  


plt.plot(x,y1,y2, color=c1, linestyle=s1, marker=m1 )

st.pyplot(fig)