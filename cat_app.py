import streamlit as st
import requests

st.set_page_config(page_title="猫猫图站", page_icon="😊")

st.markdown(
    """
    <style>
    body {
        background-color: #f9f5f0;
    }
    .stButton>button {
        background-color: #ffcccc;
        color: black;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("🐾 我的猫猫世界")
st.markdown("点击按钮，收藏属于你的喵星朋友吧！✨")


st.title("🐱 随机猫猫图")
st.write("每次点击按钮都会加载一只新猫猫～")

# 用于记录当前猫图链接（显示用）
if "current_cat_url" not in st.session_state:
    st.session_state.current_cat_url = None

# 用于保存“喜欢”的猫猫图链接
if "liked_cats" not in st.session_state:
    st.session_state.liked_cats = []

# 获取新猫猫图
if st.button("来张猫图！"):
    res = requests.get("https://api.thecatapi.com/v1/images/search")
    img_url = res.json()[0]['url']
    st.session_state.current_cat_url = img_url

# 展示猫猫图 + 喜欢按钮
if st.session_state.current_cat_url:
    st.image(st.session_state.current_cat_url, caption="喵～", use_column_width=True)

    if st.button("我喜欢它 ❤️"):
        if st.session_state.current_cat_url not in st.session_state.liked_cats:
            st.session_state.liked_cats.append(st.session_state.current_cat_url)
            st.success("已收藏这只猫猫！")

# 展示收藏的猫猫图
if st.session_state.liked_cats:
    st.markdown("---")
    st.subheader("📁 我喜欢的猫猫们：")
    for url in st.session_state.liked_cats:
        st.image(url, width=200)


