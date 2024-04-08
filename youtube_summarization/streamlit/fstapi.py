import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI()


tokenizer = AutoTokenizer.from_pretrained("Upstage/SOLAR-10.7B-Instruct-v1.0")

device = 'cuda' if torch.cuda.is_available() else 'cpu'

model = AutoModelForCausalLM.from_pretrained(
    "Upstage/SOLAR-10.7B-Instruct-v1.0",
    device_map="auto",
    torch_dtype=torch.float16,
)#.to(self.device) 
model.eval() # 모델을 평가 모드로 설정

def summarize(text):
    text = text[:4096]
    conversation = [ {'role': 'user', 'content': f'Please summarize the text by meaning chunks: \n{text}'} ] 
    
    prompt = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    #inputs_float = inputs.to(dtype=torch.float32)
    with torch.no_grad(): # 그래디언트 계산 비활성화
        outputs = model.generate(**inputs, use_cache=True, max_length=4096)
        output_text = tokenizer.decode(outputs[0])
        output_text = str.split('Assistant:')[1]
        print(output_text)
    return output_text

class SummaryRequest(BaseModel):
    text: str

# POST 메소드를 사용하는 요약 API 엔드포인트 정의
@app.post("/summarize/")
def create_summary(request: SummaryRequest):
    try:
        result = summarize(request.text)
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
