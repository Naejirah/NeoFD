from transformers import AutoTokenizer, AutoModelForCausalLM, PreTrainedModel
import transformers
import torch

#Enter your local directory you want to store the model in
save_path = "models/falcon-7b"

#Specify the model you want to download from HF
hf_model = 'tiiuae/falcon-7b'

# TODO check with accelerate

#Instantiate the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(hf_model, return_dict=True, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map="cuda",) # gpu torch_dtype=torch.bfloat16, device_map="auto",
tokenizer = AutoTokenizer.from_pretrained(hf_model)

#Save the model and the tokenizer in the local directory specified earlier
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)