from dotenv import load_dotenv
import os

# 👇 THIS is required
load_dotenv()

print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))
print("LITELLM_MODEL:", os.getenv("LITELLM_MODEL"))
