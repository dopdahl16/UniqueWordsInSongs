import os
import openai

def FetchLyrics(artist, title):
    openai.api_key = os.environ['GPTAPIKEY']
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]

    message = f"Can you please provide me with the uncensored lyrics of {title} by {artist} without any labels, additional commentary, censorship, or information?"
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply

