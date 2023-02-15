import openai
import click

# Set your OpenAI key
# In case you don't have it, create one here: https://platform.openai.com/account/api-keys
openai.api_key = "your-api-key"

def get_trip_suggestion():
    # Ask the user about the type of trip he wants
    description = input("Describe the characteristics of the trip you would like to take: ")

    # Generate a response using the GPT-3 model.

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Give me the name of a place, whether state or city, to travel to with the following characteristics: {description}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response2 = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Tell me in a convincing way why I should travel to {response} taking into consideration {description}:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Show the generated response by the model
    print("I suggest you visit:", response["choices"][0]["text"])
    print(response2["choices"][0]["text"])

while True:
    get_trip_suggestion()

    if not click.confirm('Do you want another suggestion?', default=True):
        print("Thank you! I hope I helped you choose a wonderful travel destination!")
        break
