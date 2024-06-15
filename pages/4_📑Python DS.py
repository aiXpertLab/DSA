import streamlit as st
from utils import st_def
from utils.tab_python_ds import Stack

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
# ------------------------------------------------------------------------------------------------
tab1, tab2 = st.tabs(["Stacker", "Display the Data"])

with tab1:
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.size())    # 输出：3
    print(stack.pop())     # 输出：3
    print(stack.peek())    # 输出：2
    print(stack.is_empty())     # 输出：False
