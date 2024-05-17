from openai import OpenAI

client = OpenAI(api_key="sk-proj-xP6IBb1MXBAQzmQeTQzLT3BlbkFJaOtwBEfS1B1DhCh0EjN0")

reponse = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "user", 
        "content": "Bonjour X"},
    {
        "role": "system", 
        "content": "Ok."}
  ]
)

print(reponse.choices[0].message)

