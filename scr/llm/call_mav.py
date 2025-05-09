import os
import json
import requests
from dotenv import load_dotenv

# ✅ 환경 변수에서 API Key 불러오기
load_dotenv()
API_KEY = os.getenv("FIREWORKS_API_KEY")

# ✅ API 정보
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

BASE_URL = "https://api.fireworks.ai/inference/v1/completions"
MODEL_ID = "accounts/fireworks/models/llama4-maverick-instruct-basic"

# ✅ 프롬프트와 결과 저장 경로 (사용자가 직접 값 지정하거나 비워둠)
PROMPT_PATH = ""    # ← 여기에 프롬프트 텍스트 파일 경로 지정
OUTPUT_PATH = ""    # ← 여기에 응답 저장할 파일 경로 지정

def load_prompt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()

def save_output(text, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def call_fireworks_maverick(prompt):
    payload = {
        "model": MODEL_ID,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 0.9,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.0,
        "stop": ["\n\n", "<|endoftext|>"]
    }

    print("✅ Sending prompt to Maverick API...")
    response = requests.post(BASE_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    data = response.json()
    # Fireworks 응답 구조: choices[0]["text"]
    return data["choices"][0]["text"].strip()

def main():
    if not PROMPT_PATH or not OUTPUT_PATH:
        print("❗ PROMPT_PATH, OUTPUT_PATH를 지정하세요.")
        return

    prompt = load_prompt(PROMPT_PATH)
    response_text = call_fireworks_maverick(prompt)
    save_output(response_text, OUTPUT_PATH)

    print("✅ 응답 저장 완료!")

if __name__ == "__main__":
    test_prompt = "인스타그램 게시물을 분석하여 광고성 여부를 판단하고 이유를 설명하세요."
    response = call_fireworks_maverick(test_prompt)
    print("✅ 응답:", response)

    with open("ans.txt", "w", encoding="utf-8") as f:
        f.write(response)

    print("✅ 응답이 ans.txt에 저장되었습니다.")

