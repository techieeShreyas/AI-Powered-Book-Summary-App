import markdown 
import os
from django.utils.safestring import mark_safe
from django.shortcuts import render
from PyPDF2 import PdfReader
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    # api_key="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"
    # api_key="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"
    api_key=os.getenv("OPENAI_API_KEY")

)

def index(request):
    summary = None
    if request.method == "POST" and request.FILES.get("pdf_file"):
        pdf_file = request.FILES["pdf_file"]
        role = request.POST.get("role")
        interest = request.POST.get("interest")

        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        # Interest prompt logic
        if interest == "general":
            user_prompt = f"Summarize this book for a {role}. Provide key points in bullet points.\n\n{text}"
        else:
            user_prompt = f"Summarize this book for a {role}, focusing on the theme of {interest}. If no related content is found, give a general summary.\n\n{text}"

        # Uncomment when using OpenAI API
        # response = client.chat.completions.create(
        #     # model="deepseek/deepseek-chat-v3.1:free",
        #       model="mistralai/mistral-nemo:free",
        #     messages=[{"role": "user", "content": user_prompt}]
        # )

        # print(response)
        # raw_summary = response.choices[0].message.content
        # raw_summary = f"### (Demo) Summary for role: {role}, interest: {interest}\n\n- Key idea 1...\n- Key idea 2..."
        
        # summary = mark_safe(markdown.markdown(raw_summary))
        summary="hello, i am here."
    return render(request, "summarizer/front.html", {"summary": summary})
