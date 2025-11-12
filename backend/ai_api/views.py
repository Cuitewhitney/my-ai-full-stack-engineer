from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Enhancement
from .serializers import EnhancementSerializer
import os
from dotenv import load_dotenv
load_dotenv()

# Lazy OpenAI client – only create if key exists
def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        from openai import OpenAI
        return OpenAI(api_key=api_key)
    return None

class EnhanceView(APIView):
    def post(self, request):
        text = request.data.get("text", "").strip()
        if not text:
            return Response({"error": "No text provided"}, status=400)

        client = get_openai_client()
        if client:
            # REAL GPT-4o
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a professional writer. Enhance the text to sound polished and professional."},
                    {"role": "user", "content": text}
                ],
                max_tokens=300
            )
            enhanced = response.choices[0].message.content
        else:
            # FREE FALLBACK MODE (no key needed)
            enhanced = f"PROFESSIONAL VERSION:\n\n\"{text.upper()}\"\n\n– Your AI Fullstack Engineer (Add OPENAI_API_KEY for real GPT)"

        # SAVE TO DATABASE
        enhancement = Enhancement.objects.create(original=text, enhanced=enhanced)
        return Response({"enhanced": enhanced})

class HistoryView(APIView):
    def get(self, request):
        history = Enhancement.objects.all().order_by('-created_at')
        serializer = EnhancementSerializer(history, many=True)
        return Response(serializer.data)