import streamlit as st
from streamlit_player import st_player

import customwhisper as cw
import ytextract as ext

import requests

st.header('Youtube summarize')

if "input" not in st.session_state:
    st.session_state["input"] = ""
if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.form(key="my_form", clear_on_submit=True):
    col1, col2 = st.columns([7, 1])

    with col1:
        st.text_input(
            "Paste youtube URL",
            placeholder="paste youtube URL",
            key="input",
        )
    with col2:
        st.write("&#9660;&#9660;&#9660;")
        submit = st.form_submit_button(label="start")

if submit:
    msg = (st.session_state["input"], True)
    st.write(msg)
    st.session_state.messages.append(msg)
    fulltitle = ext.download_video(msg[0])
    st_player(msg[0])
    script = cw.stt(fulltitle)

    with st.form(key="r", clear_on_submit=True):
        col1, col2 = st.columns([1, 1])

        with col1:
            st.write(script["text"])
        with col2:
            st.write("&#9660;&#9660;&#9660;")
            url = "http://10.28.224.198:8000/summarize/"
            
            # 요청 데이터
            data = {"text": script["text"]}
            
            # POST 요청으로 FastAPI 서버에 데이터 전송
            response = requests.post(url, json=data)
            
            if response.status_code == 200:
                # 결과 처리 및 출력
                result = response.json()
                st.write(result["summary"])
            else:
                st.error("오류가 발생했습니다.")
