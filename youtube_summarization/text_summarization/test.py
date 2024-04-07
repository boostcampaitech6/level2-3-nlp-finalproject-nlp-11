import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import re

tokenizer = AutoTokenizer.from_pretrained("Upstage/SOLAR-10.7B-Instruct-v1.0")
model = AutoModelForCausalLM.from_pretrained(
    "Upstage/SOLAR-10.7B-Instruct-v1.0",
    device_map="auto",
    torch_dtype=torch.float16,
)
max_length = 4096

f = open('../text_summarization/title.txt', 'r')
sample_title = f.read()
f.close()

f = open('../stt/'+sample_title+'.txt', 'r')
sample_text = f.read()
f.close()

def prompting_n_tokenize(sample_text, sample_title, tokenizer):
    sample_text = re.sub('[^가-힣A-Za-z\d\s.?,]','', sample_text)
    sample_text = re.sub('\s+', ' ', sample_text)
    conversation = [ {'role': 'user', 'content': f'텍스트의 제목이 "{sample_title}"일 때, 아래의 텍스트를 내용별로 분할하고, 분할된 내용을 각각 요약하여 목록으로 보여줘. (수식이 있다면 임의로 계산하지 말고 그대로 보여주되, 중요한 내용이 아니면 가져오지 마. 영상에 좋아요를 누르거나 영상을 구독해 달라는 내용은 요약하지 마.): \n###텍스트: {sample_text}'} ] 
    prompt = tokenizer.apply_chat_template(conversation, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    return inputs

def summarize(inputs, tokenizer, model, max_length):
    outputs = model.generate(**inputs, use_cache=True, max_length=max_length)
    output_text = tokenizer.decode(outputs[0]) 
    output_test = re.sub()
    return output_text

total_output_text = ''
if len(sample_text) > 2000:
    chunks = [sample_text[i:i+2000] for i in range(0, len(sample_text), 2000)]
    for chunk in chunks:
        chunk_inputs = prompting_n_tokenize(chunk, sample_title, tokenizer)
        total_output_text += summarize(chunk_inputs, tokenizer, model, max_length)

f = open('./'+sample_title+'.txt', 'w')
f.write(total_output_text)
f.close()
