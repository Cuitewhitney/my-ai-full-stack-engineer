from rest_framework.views import APIView
from rest_framework.response import Response
from openai import OpenAI
import os
from .models import Enhancement
from .serializers import EnhancementSerializer

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class EnhanceView(APIView):
    def post(self, request):
        text = request.data.get("text", "")
        if not text:
            return Response({"error": "No text provided"}, status=400)

        # FREE AI MODE (change to real OpenAI later)
        enhanced = "PROFESSIONAL VERSION: " + text.upper()

        # SAVE TO DATABASE
        enhancement = Enhancement.objects.create(original=text, enhanced=enhanced)

        return Response({"enhanced": enhanced})

class HistoryView(APIView):
    def get(self, request):
        history = Enhancement.objects.all().order_by('-created_at')
        serializer = EnhancementSerializer(history, many=True)
        return Response(serializer.data)