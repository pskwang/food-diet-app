import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

# ── 1. 엑셀 로드 ──────────────────────────────────────────
file_path = r"C:\Users\COM\Desktop\데이터 분석\팀플\food-diet-app\20251229_음식DB 19495건.xlsx"
df = pd.read_excel(file_path, header=0)

# 컬럼명 공백 제거
df.columns = df.columns.str.strip()

# ── 2. 필요한 컬럼만 추출 ─────────────────────────────────
columns_map = {
    "식품명":           "food_name",
    "식품대분류명":      "category",
    "영양성분함량기준량": "serving_size",
    "에너지(kcal)":     "calories",
    "탄수화물(g)":      "carbs",
    "단백질(g)":        "protein",
    "지방(g)":          "fat",
    "나트륨(mg)":       "sodium",
    "당류(g)":          "sugar",
    "식이섬유(g)":      "fiber",
}

df = df[list(columns_map.keys())].rename(columns=columns_map)

# ── 3. 클렌징 ─────────────────────────────────────────────
df = df.dropna(subset=["food_name"])
df = df.fillna(0)
df["food_name"] = df["food_name"].str.strip()

numeric_cols = ["calories", "carbs", "protein", "fat", "sodium", "sugar", "fiber"]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce").fillna(0)

print(f"✅ 총 {len(df)}개 식품 데이터 준비 완료")
print(df.head(3))

# ── 4. MySQL 적재 ─────────────────────────────────────────
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST     = os.getenv("DB_HOST")
DB_NAME     = os.getenv("DB_NAME")

password = quote_plus(DB_PASSWORD)
DB_URL = f"mysql+pymysql://{DB_USER}:{password}@{DB_HOST}/{DB_NAME}?charset=utf8mb4"
engine = create_engine(DB_URL)

df.to_sql("foods", con=engine, if_exists="replace", index=False)
print("✅ MySQL foods 테이블 적재 완료!")