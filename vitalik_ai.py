import openai
import os

class VitalikAI:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")  # Store API key securely

    def generate_tweet(self, prompt):
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Or another suitable model
                messages=[
                    {"role": "system", "content": "You are Vitalik Buterin, the co-founder of Ethereum. Respond as Vitalik Buterin, sharing your thoughts on crypto."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=140,  # Tweet length constraint
                n=1,
                stop=None,
                temperature=0.7,  # Adjust for creativity
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error generating tweet: {e}"