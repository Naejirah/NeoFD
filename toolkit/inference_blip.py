import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

save_path = "IA/blip/models"

processor = BlipProcessor.from_pretrained(save_path)
model = BlipForConditionalGeneration.from_pretrained(save_path)

# img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
img_url = 'outputs/txt2img-samples/samples/00008.png'
# raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')
raw_image = Image.open(img_url).convert('RGB')

# conditional image captioning
text = "a photography of"
inputs = processor(raw_image, text, return_tensors="pt")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))
# >>> a photography of a woman and her dog

# unconditional image captioning
inputs = processor(raw_image, return_tensors="pt")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))
