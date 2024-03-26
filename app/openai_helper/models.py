GPT_3_5 = "gpt-3.5-turbo"
GPT_3_5_16K = "gpt-3.5-turbo-16k"
GPT_4 = "gpt-4"

class GPTConfig:
    def __init__(self, model=GPT_3_5, temperature=0, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0, stop=[""]):
        self.model = model
        self.temperature = temperature
        self.max_tokens =max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = stop

    def __str__(self):
        return f"Model: {self.model}, Temperature: {self.temperature}"