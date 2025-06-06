from google import genai
from google.genai import types
import base64

client = genai.Client(
    vertexai=True,
    project="quantum-beach-393003",
    location="us-central1",
)
def generatePlantDiseaseInformation(base64_image):
    # return "This is a placeholder response"

    image1 = types.Part.from_bytes(
        data=base64.b64decode(base64_image),
        mime_type="image/jpeg",
    )
    text1 = types.Part.from_text(text="""identify the plant shown in the image name any disease present on the plant and an approximate percentage in number in the table with one column for a description of the plant and disease, and provide extra notes if needed""")

    model = "gemini-2.0-flash-001"
    contents = [
        types.Content(
        role="user",
        parts=[
            image1,
            text1
        ]
        )
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature = 0.5,
        top_p = 0.95,
        max_output_tokens = 8192,
        response_modalities = ["TEXT"],
        safety_settings = [types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="OFF"
        )],
    )
    response=""
    for chunk in client.models.generate_content_stream(
        model = model,
        contents = contents,
        config = generate_content_config,
        ):
        response+=chunk.text
        print(chunk.text, end="")
    return response

def generateGeneralResponse(text_input):
    text1 = types.Part.from_text(text=text_input)

    model = "gemini-2.0-flash-001"
    contents = [
        types.Content(
        role="user",
        parts=[
            text1
        ]
        )
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature = 0.5,
        top_p = 0.95,
        max_output_tokens = 8192,
        response_modalities = ["TEXT"],
        safety_settings = [types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="OFF"
        ),types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="OFF"
        )],
    )
    response=""
    for chunk in client.models.generate_content_stream(
        model = model,
        contents = contents,
        config = generate_content_config,
        ):
        response+=chunk.text
        print(chunk.text, end="")
    return response

print(generateGeneralResponse("What is the capital of France?"))