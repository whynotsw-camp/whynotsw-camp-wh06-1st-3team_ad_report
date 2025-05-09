# scr/path.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# config
CONFIG_DIR = os.path.join(BASE_DIR, "config")
DB_CONFIG_PATH = os.path.join(CONFIG_DIR, "db_config.json")
MAV_CONFIG_PATH = os.path.join(CONFIG_DIR, "mav_config.json")
PROMPT_TEMPLATES_PATH = os.path.join(CONFIG_DIR, "prompt_templates.py")

# data
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
POST_PARSED_DIR = os.path.join(DATA_DIR, "post_parsed")
LLM_PARSED_POST_DIR = os.path.join(DATA_DIR, "llm_parsed_post")
LLM_PARSED_AD_DIR = os.path.join(DATA_DIR, "llm_parsed_ad")

# db
DB_DIR = os.path.join(BASE_DIR, "db")
SCHEMA_SQL_PATH = os.path.join(DB_DIR, "schema.sql")

# scr
SCR_DIR = os.path.join(BASE_DIR, "scr")
DATA_COLLECTION_DIR = os.path.join(SCR_DIR, "data_collection")
LLM_DIR = os.path.join(SCR_DIR, "llm")
PARSING_DIR = os.path.join(SCR_DIR, "parsing")
PROMT_DIR = os.path.join(SCR_DIR, "promt")
SCORING_DIR = os.path.join(SCR_DIR, "scoring")

# 기타
NOTEBOOKS_DIR = os.path.join(BASE_DIR, "notebooks")
README_PATH = os.path.join(BASE_DIR, "README.md")
REQUIREMENTS_PATH = os.path.join(BASE_DIR, "requirements.txt")
ENV_PATH = os.path.join(BASE_DIR, ".env")

# logs (필요 시)
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# 각 파일별 직접 경로 필요할 때는 아래처럼 추가 가능
CRON_SCRIPT_PATH = os.path.join(SCR_DIR, "cron.sh")
