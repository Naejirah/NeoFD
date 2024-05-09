from transformers import AutoTokenizer, AutoModelForCausalLM, PreTrainedModel
import transformers
import torch
save_path = "IA/falcon/models/falcon-7b"

# #Empty GPU cache HEREGPU
torch.cuda.empty_cache()

# #Define the batch size and load the model's dataset
dataset = "IA/falcon/models/falcon-7b"
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
  "Girafatron is obsessed with giraffes, the most glorious animal on the face of this Earth. Giraftron believes all other animals are irrelevant when compared to the glorious majesty of the giraffe.\nDaniel: Hello, Girafatron!\nGirafatron:",
   max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=local_tokenizer.eos_token_id,
)

#Output the inference
for seq in sequences:
    print(f"Result: {seq['generated_text']}")