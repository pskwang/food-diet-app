# 🍱 오늘 뭐 먹지? — 식단 기록 & 영양소 분석 서비스

![GitHub branch](https://img.shields.io/badge/branch-dev-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.135-009688)
![React](https://img.shields.io/badge/React-18-61DAFB)

## 📌 프로젝트 소개
오늘 먹은 음식을 기록하면 영양소를 자동 분석하고 시각화해주는 웹 서비스입니다.
식약처 공공 데이터 19,495건을 기반으로 칼로리, 단백질, 탄수화물 등 영양 정보를 제공합니다.

## 👥 팀원 및 역할
| 이름 | 역할 | 담당 |
|------|------|------|
| pskwang | 데이터 분석 / 백엔드 | Python, FastAPI, MySQL |
| 친구이름 | 프론트엔드 | React, Recharts, Tailwind CSS |

## 🛠️ 기술 스택
**Backend**
- Python, FastAPI, SQLAlchemy
- MySQL, pandas

**Frontend**
- React, Axios, Recharts, Tailwind CSS

## 📂 프로젝트 구조
```
food-diet-app/
├── backend/
│   ├── main.py          # FastAPI 서버 & API 엔드포인트
│   ├── database.py      # MySQL 연결 설정
│   ├── models.py        # DB 테이블 모델
│   ├── preprocess.py    # 식약처 데이터 전처리
│   └── requirements.txt
└── frontend/
    └── src/             # React 소스코드
```

## 🔌 API 명세
| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/foods/search?name=김밥` | 음식 검색 |
| GET | `/foods/analyze?name=김밥` | 영양소 분석 |
| POST | `/records` | 식단 기록 저장 |
| GET | `/records` | 식단 기록 조회 |

## 🚀 실행 방법

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm start
```

## 📊 데이터 출처
- [식품안전나라 식품영양성분DB](https://various.foodsafetykorea.go.kr/nutrient)
- 총 19,495건 음식 데이터