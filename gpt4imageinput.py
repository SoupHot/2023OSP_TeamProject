import openai
import base64
import requests
import re

# OpenAI API Key

def generate_midi_from_image(api_key, image_path):
    # ===================================================
    # 이미지 경로가 아니라 이미지 파일 객체로 함수 수행
    def encode_image(image_file):
        return base64.b64encode(image_file.read()).decode('utf-8')
    # 파일 객체를 다시 처음으로 되돌림
    image_path.seek(0)
    # base64 문자열을 가져옴
    base64_image = encode_image(image_path)
    # ===================================================
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Generate a MIDI file with notes that match the mood of this image. Play only notes that match the mood for 30 seconds. For example, E4 D4 C4 D4 E4 E4 D4 D4 D4 D4 E4 G4 G4 G4 without any explanation."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_json = response.json()
        content_text = response_json.get("choices", [])[0].get("message", {}).get("content", "")
        notes = re.findall(r'\b[A-G][#b]?[0-9]\b', content_text)
        notes_text = ' '.join(notes)
        return notes_text
    else:
        return "Error in API request"

# Example usage
# image_path = "/content/drive/MyDrive/teamproject/friends.jpg"
# print(generate_midi_from_image(image_path))

