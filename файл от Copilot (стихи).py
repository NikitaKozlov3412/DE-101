import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Загрузка предварительно обученной модели и токенизатора (например, gpt2)
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Функция генерации стихов
def generate_poem(prompt, max_length=100, temperature=0.7, num_return_sequences=1):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        temperature=temperature,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        num_return_sequences=num_return_sequences
    )
    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

if __name__ == "__main__":
    prompt = "В тихий вечер, под шёпот ветра,"
    poems = generate_poem(prompt, max_length=100, temperature=0.8)
    for idx, poem in enumerate(poems):
        print(f"--- Стихотворение {idx+1} ---")
        print(poem)
