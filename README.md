# 한닢튜브
<img width="588" alt="스크린샷 2024-03-27 12 08 50" src="https://github.com/boostcampaitech6/level2-3-nlp-finalproject-nlp-11/assets/97589999/0d3e1c6d-9a1c-4bfa-81df-268f77c1c20a">



동전 한 닢처럼 가볍게, 한 입에 먹는 영상!  한닢튜브를 소개합니다~!!

이 프로젝트는 바쁜 현대인을 위한 유튜브 영상 요약 서비스입니다.

# Members
- 박산야
  - 영상 주소를 이용한 유튜브 영상
          추출 및 OpenAI Whisper 모델을
          이용한 STT 과정 구현
  - Upstage의 Solar 10.7B LLM을
          비롯한 여러 모델의 프롬프트를
          통한 텍스트 요약 구현 및 성능
          개선 실험


- 박준우
  - 웹페이지 제작
  - 서비스 시간 단축 방안 연구
  - stt/텍스트요약 모델 관련 실험 보조
    
- 함문정: 모델 탐색 및 고도화
  - 요약 모델 탐색
  - stt 모델 처리 속도 및 성능 개선

# Respository Structure
<pre><code>{code}</code></pre>

# Installation
<pre><code>
pip install pytube
sudo apt update && sudo apt install ffmpeg
pip install transformers
pip install streamlit
pip install streamlit_player
    
</code></pre>

# Download Pre-Trained Models

### 1. STT (whisper)
<pre><code>
pip3 install git+https://github.com/openai/whisper.git
pip3 install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
    
</code></pre>

### 2. Text Summarization (Solar)
<pre><code>
tokenizer = AutoTokenizer.from_pretrained("Upstage/SOLAR-10.7B-Instruct-v1.0")
model = AutoModelForCausalLM.from_pretrained(
    "Upstage/SOLAR-10.7B-Instruct-v1.0",
    device_map="auto",
    torch_dtype=torch.float16,
)
    
</code></pre>

# How to Use
<pre><code>
pip install -r requirements.txt
streamlit run ytsummarize.py
  
</code></pre>

# Demo

# Project Review
https://boostcampait.notion.site/NLP-11-Forgotten-Items-169ab27b5e544b8293e01b0cbafb7a12
