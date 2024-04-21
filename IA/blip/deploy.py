from transformers import AutoTokenizer, BlipProcessor, BlipForConditionalGeneration
import transformers
import torch

#Enter your local directory you want to store the model in
save_path = "models"

#Specify the model you want to download from HF
hf_model = 'Salesforce/blip-image-captioning-base'

#Instantiate the model and tokenizer
processor = BlipProcessor.from_pretrained(hf_model) # gpu torch_dtype=torch.bfloat16, device_map="auto",
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
tokenizer = AutoTokenizer.from_pretrained(hf_model)

#Save the model and the tokenizer in the local directory specified earlier
processor.save_pretrained(save_path)
model.save_pretrained(save_path)
tokenizer.save_pretrained(save_path)