from settings import SYSTEM


def gpt_4o_response(client, request, system=SYSTEM):
    response = client.chat.complete(
        model='mistral-large-latest',
        messages=[
            {"role": "user", "content": request},
        ],
    )
    return response.choices[0].message.content
