import requests
import argparse
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def launch_blip(path, img):

    save_path = path

    processor = BlipProcessor.from_pretrained(save_path)
    model = BlipForConditionalGeneration.from_pretrained(save_path)

    # img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
    img_url = img
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

def main():
    """

    :return:
    """

    parser = argparse.ArgumentParser(description='Lancement de blip', usage="""
        inference.py launch  """)

    # Positional arguments
    parser.add_argument('command', choices=['launch'],
                        help='Specify the command')
    
    launch_group = parser.add_argument_group('Launch Options',
                                               argument_default=argparse.SUPPRESS)
    launch_group.add_argument('-path', type=str, default="IA/blip/models/blip-image-captioning-base", dest='path',
                                help='Chemin du modèle')
    launch_group.add_argument('-img', type=str, default="outputs/txt2img-samples/samples/00008.png", dest='img',
                                help='Chemin de l\'image en entrée')
    
    args = parser.parse_args()

    launch_blip(args.path, args.img)

if __name__ == "__main__":
    main()




