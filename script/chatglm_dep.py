from transformers import AutoTokenizer, AutoModel,GenerationConfig
import os
os.environ['CUDA_VISIBLE_DEVICES'] = "7"
import torch
import warnings
warnings.filterwarnings("ignore")

model_path = "/data/ubuntu/public/models/chatglm_6b"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)

model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
generate_config = GenerationConfig(
     max_length = 512,
     min_length = 10,
     do_sample = False,
     temperature = 0.1
 )

while True:

    input_text = input("问题:")
    
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.cuda()
    
    outputs = model.generate(input_ids,generation_config = generate_config)
    
    output_text = tokenizer.decode(outputs[0]).split(input_text)
    
    print("ChatGLM:"+output_text[-1])

