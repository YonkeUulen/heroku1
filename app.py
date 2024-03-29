import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

#st.latex(r'a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} = \sum_{k=0}^{n-1} ar^k = a \left(\\frac{1-r^{n}}{1-r}\\right)')
st.header('Schmallndotz!')
st.write(df)