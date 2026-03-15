from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db, engine
from models import Base, Record

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS 설정 (React 연동용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── 1. 음식 검색 API ──────────────────────────────────────
@app.get("/foods/search")
def search_foods(name: str = Query(...), db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM foods WHERE food_name LIKE :name LIMIT 20"),
        {"name": f"%{name}%"}
    ).fetchall()
    return [dict(row._mapping) for row in result]

# ── 2. 영양소 분석 API ────────────────────────────────────
@app.get("/foods/analyze")
def analyze_food(name: str = Query(...), db: Session = Depends(get_db)):
    result = db.execute(
        text("SELECT * FROM foods WHERE food_name = :name LIMIT 1"),
        {"name": name}
    ).fetchone()
    if not result:
        return {"error": "음식을 찾을 수 없어요"}
    return dict(result._mapping)

# ── 3. 식단 기록 저장 API ─────────────────────────────────
@app.post("/records")
def add_record(food_name: str, calories: float, carbs: float,
               protein: float, fat: float, sodium: float,
               sugar: float, fiber: float, db: Session = Depends(get_db)):
    record = Record(
        food_name=food_name, calories=calories, carbs=carbs,
        protein=protein, fat=fat, sodium=sodium,
        sugar=sugar, fiber=fiber
    )
    db.add(record)
    db.commit()
    return {"message": "기록 완료!"}

# ── 4. 식단 기록 조회 API ─────────────────────────────────
@app.get("/records")
def get_records(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM records ORDER BY date DESC")).fetchall()
    return [dict(row._mapping) for row in result]