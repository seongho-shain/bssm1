import streamlit as st

# 이미지 URL 또는 로컬 경로 설정
image_urls = [
    "https://via.placeholder.com/150",
    "https://via.placeholder.com/150/0000FF",
    "https://via.placeholder.com/150/008000"
]

# HTML로 이미지 표시
image_options = [f'<img src="{url}" width="150">' for url in image_urls]

# 라디오 버튼 생성
selected_image = st.radio("Choose an image:", options=image_options, format_func=lambda x: x)


# 선택된 이미지 표시
st.markdown(f'You selected: {selected_image}', unsafe_allow_html=True)
