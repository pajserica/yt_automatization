import openai

openai.api_key = "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"

topic = input("topic of request('actor', 'city', 'motorbike') optional..")
request = input("write request (start with 'top 10 ...'): ")

with open(r"C:\Users\PAJSER-PC\Desktop\Test Programi\TOP_10\requests.txt", "w") as f:
    f.write(request + "\n" + topic + "\n")

response1 = openai.Completion.create(
    engine="text-davinci-003",
    prompt=f"Write me {request} without any additional words",
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=1,
)
result = response1["choices"][0]["text"]

#print(result)

with open(r"C:\Users\PAJSER-PC\Desktop\Test Programi\TOP_10\requests.txt", "a") as f:
    f.write(result.strip() + "\n")