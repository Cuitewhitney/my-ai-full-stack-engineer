from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Enhancement
from .serializers import EnhancementSerializer
import os

class EnhanceView(APIView):
    def post(self, request):
        text = request.data.get("text", "").strip()
        if not text:
            return Response({"error": "No text provided"}, status=400)

        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            try:
                from openai import OpenAI
                client = OpenAI(api_key=api_key)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Enhance this text to be professional and polished."},
                        {"role": "user", "content": text}
                    ],
                    max_tokens=300
                )
                enhanced = response.choices[0].message.content
            except Exception as e:
                enhanced = f"[AI ERROR: {str(e)}] FALLBACK: {text.upper()}"
        else:
            enhanced = f"PROFESSIONAL (FREE MODE):\n\n\"{text.upper()}\"\n\n(Add OPENAI_API_KEY for real AI)"

        enhancement = Enhancement.objects.create(original=text, enhanced=enhanced)
        return Response({"enhanced": enhanced})

class HistoryView(APIView):
    def get(self, request):
        history = Enhancement.objects.all().order_by('-created_at')
        serializer = EnhancementSerializer(history, many=True)
        return Response(serializer.data)