from openai import OpenAI, RateLimitError
import dotenv
import os

dotenv.load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
try:
    resposta = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role": "system",
                "content": "Gere nomes de produtos fictícios sem descrição de acordo com a requisição do usuário."
            },
            {
                "role": "user",
                "content": "Gere 5 produtos"
            } 
        ]
    )
    print(resposta)
except RateLimitError as err:
    print("Limite de requisições a API OpenAI alcançado, verifique seus créditos em: https://platform.openai.com/account/billing/overview")
