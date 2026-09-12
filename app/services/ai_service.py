import requests
from config import Config


class AIServiceError(Exception):
    """Yapay zeka servisine ozel hata sinifi."""
    pass


class AIService:
    """Groq API ile konusan servis katmani. Flask, HTTP veya veritabani
    kavramlarini bilmez, sadece yapay zeka ile konusur."""

    def __init__(self):
        self.api_key = Config.GROQ_API_KEY
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.model = "llama-3.1-8b-instant"

    def _sistem_talimati(self):
        """BUSINESS_CONTEXT'i config'den okuyan yardimci metot."""
        return Config.BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        """Kullanici mesajini alip Groq'a gonderir, yaniti dondurur."""
        if not self.api_key:
            return "Demo modundayiz: Groq API anahtari henuz tanimlanmadi."

        if gecmis is None:
            gecmis = []

        messages = [{"role": "system", "content": self._sistem_talimati()}]
        messages.extend(gecmis)
        messages.append({"role": "user", "content": mesaj})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": messages
        }

        try:
            response = requests.post(
                self.api_url, headers=headers, json=payload, timeout=15
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]
        except Exception as e:
            raise AIServiceError(f"Yapay zeka servisi hatasi: {e}")


ai_service = AIService()
