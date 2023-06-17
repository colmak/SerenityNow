import os
import openai
import gradio as gr

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "Incude a summary at the beginning of the message. Also include a message of support at the start. Imagine that you're meeting with a new client for the first time. They're feeling anxious and overwhelmed about their current life situation, and they've come to you for guidance and support. Your goal as a therapist is to create a safe and welcoming space where your client feels heard and understood. You want to convey empathy and compassion, and help them explore their thoughts and feelings in a non-judgmental way. How would you approach this situation as a caring and kind therapist who genuinely wants to help people?"},
]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.inputs.Textbox(lines=7, label="SerenityNow")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="SerenityNow",
             description="How can I help you?", interface_color="#6C8D80",
             theme="compact").launch(share=True)
