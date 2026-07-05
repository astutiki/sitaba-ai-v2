import requests

SITABA_PUBLICATION_API = "https://sitaba.pu.go.id/api-public/noauth/publication"

def proses_publication(question):

    try:

        response = requests.get(
            SITABA_PUBLICATION_API,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        keyword = question.lower()

        for item in data.get("data", []):

            title = item.get("title", "").lower()

            if keyword in title:

                return {
                    "reply":
                        f"{item['title']}\n\n"
                        f"{item.get('description','')}\n\n"
                        f"{item.get('url','')}"
                }

        return {
            "reply":"Publikasi tidak ditemukan."
        }

    except Exception as e:

        return {
            "reply":f"Gagal mengambil publikasi : {e}"
        }