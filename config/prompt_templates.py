# config/prompt_templates.py

def build_analysis_prompt(caption: str, hashtags: list, url: str) -> str:
    """
    게시물에 대한 분석 기준을 요구하는 프롬프트 생성
    """
    hashtags_str = ", ".join(hashtags)
    
    prompt = f"""
다음은 인스타그램 게시물의 정보입니다.

- 캡션:
{caption}

- 해시태그:
{hashtags_str}

- URL:
{url}

이 게시물을 기반으로 아래 정보를 분석해줘:
1. 이 게시물이 속할 수 있는 분야/카테고리
2. 게시물에서 드러나는 관심사 키워드 5개 이내
3. 게시물의 주제를 한 문장으로 요약
4. 게시물의 타겟 오디언스 추정 (예: MZ세대, 30대 여성 등)

명확하고 간결하게 응답해줘.
"""
    return prompt.strip()


def build_ad_prompt(caption: str, hashtags: list, url: str) -> str:
    """
    게시물의 광고 여부 및 광고 관련 정보를 요청하는 프롬프트 생성
    """
    hashtags_str = ", ".join(hashtags)
    
    prompt = f"""
다음은 인스타그램 게시물의 정보입니다.

- 캡션:
{caption}

- 해시태그:
{hashtags_str}

- URL:
{url}

이 게시물이 광고성 또는 협찬 게시물인지 판단해줘.
다음 정보를 JSON 형식으로 반환해줘:

{{
  "is_ad": (true 또는 false),
  "is_sponsored": (true 또는 false),
  "ad_score": (0.0 ~ 1.0 사이 float),
  "ad_keywords": ["광고성 판단 키워드1", "광고성 판단 키워드2", ...],
  "sponsored_keywords": ["협찬 판단 키워드1", "협찬 판단 키워드2", ...],
  "reason": "광고 또는 협찬으로 판단한 이유를 한 문장으로 설명"
}}

응답은 반드시 위 JSON 구조를 따르고, 추가 설명 없이 JSON만 출력해줘.
"""
    return prompt.strip()
