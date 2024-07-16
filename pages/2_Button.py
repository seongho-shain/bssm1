import streamlit as st
st.button("BYE")
if st.button("HI"):
    st.session_state.key = "Hi"
else :
    st.session_state.key = "Bye"

#Main page - 소개 및 학번 이름 입력
##Quiz - 주관식 한 문제(50점), 객관식 한 문제(50점) / 다음 누르면 Result
##Result - 입력된 학번 이름 띄우고 점수도 띄워요