import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4, 44, 55],
    'second column': [10, 20, 30, 40, 400, 500]
})

st.write(df)