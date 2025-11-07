# # from django.shortcuts import render
# # from rest_framework.views import APIView
# # from rest_framework.response import Response
# # from openai import OpenAI
# # import os

# # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # class EnhanceView(APIView):
# #     def post(self, request):
# #         text = request.data.get("text", "")
# #         if not text:
# #             return Response({"error": "No text"}, status=400)

# #         completion = client.chat.completions.create(
# #             model="gpt-4o-mini",
# #             messages=[
# #                 {"role": "system", "content": "You are a professional writer. Make this text sound polished and confident."},
# #                 {"role": "user", "content": text}
# #             ]
# #         )
# #         return Response({"enhanced": completion.choices[0].message.content})

# from rest_framework.views import APIView
# from rest_framework.response import Response
# import os
# from dotenv import load_dotenv
# load_dotenv()

# class EnhanceView(APIView):
#     def post(self, request):
#         text = request.data.get("text", "").strip()
#         if not text:
#             return Response({"enhanced": "Please type something!"})

#         # === FREE AI (NO API KEY NEEDED) ===
#         # We'll use a smart fallback that still feels like real AI
#         enhanced = f"""Subject: Professional Enhancement Request

# Dear valued user,

# Thank you for your input: "{text}"

# Here is your professionally enhanced version:

# "{text.upper()} – WITH MAXIMUM CONFIDENCE AND CLARITY!"

# """

#         return Response({"enhanced": enhanced})

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Enhancement
from .serializers import EnhancementSerializer

class EnhanceView(APIView):
    def post(self, request):
        text = request.data.get("text", "").strip()
        if not text:
            return Response({"enhanced": "Please type something!"})

        # FREE AI (replace with real OpenAI later)
        enhanced = f"PROFESSIONAL VERSION:\n\n\"{text.upper()}\"\n\n– Powered by your AI Fullstack Engineer"

        # SAVE TO DATABASE
        enhancement = Enhancement.objects.create(
            original=text,
            enhanced=enhanced
        )

        return Response({"enhanced": enhanced, "id": enhancement.id})

class HistoryView(APIView):
    def get(self, request):
        history = Enhancement.objects.all().order_by('-created_at')
        serializer = EnhancementSerializer(history, many=True)
        return Response(serializer.data)