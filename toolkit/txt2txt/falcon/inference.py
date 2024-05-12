from transformers import AutoTokenizer, AutoModelForCausalLM, PreTrainedModel
import transformers
import torch
import argparse

def launch_falcon(path, input):

    save_path = path

    # #Empty GPU cache HEREGPU
    torch.cuda.empty_cache()

    # #Define the batch size and load the model's dataset
    dataset = path
    torch.utils.data.DataLoader(dataset, batch_size=1)

    #Load the model and tokenizer from local storage
    local_model = AutoModelForCausalLM.from_pretrained(save_path, return_dict=True, trust_remote_code=True, device_map="cuda",torch_dtype=torch.bfloat16).to("cuda") #GPU
    # local_model = AutoModelForCausalLM.from_pretrained(save_path, return_dict=True, trust_remote_code=True) #CPU
    local_tokenizer = AutoTokenizer.from_pretrained(save_path) #2
    pipeline = transformers.pipeline(
        "text-generation",
        model=local_model,
        tokenizer=local_tokenizer,
        torch_dtype=torch.bfloat16,
    )
    # pipeline = transformers.pipeline(
    #     "text-generation",
    #     model=local_model,
    #     tokenizer=local_tokenizer,
    # ) #CPU

    #Prompt the model with the required parameters
    sequences = pipeline(
    input,
    max_length=200,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=local_tokenizer.eos_token_id,
    )

    #Output the inference
    for seq in sequences:
        print(f"Result: {seq['generated_text']}")

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
    launch_group.add_argument('-modele', type=str, default="IA/falcon/models/falcon-7b", dest='model',
                                help='Chemin du modèle')
    launch_group.add_argument('-input', type=str, default="Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:", dest='input',
                                help='Chemin de l\'input d\'entrée')
    
    args = parser.parse_args()

    launch_falcon(args.model, args.input)

if __name__ == "__main__":
    main()
