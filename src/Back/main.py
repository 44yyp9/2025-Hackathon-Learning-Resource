from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import Printer
import SqlConecter


app = FastAPI()

# CORS設定（フロントと通信可能にする）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "FastAPI backend is running on Vercel"}

# ランダムな数字を生成してDBに保存するエンドポイント
@app.post("/print")
async def print_result():
    printNumber=Printer.Printer().print_message()
    conn=SqlConecter.SqlConecter.get_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO draws (number) VALUES (%s)", (printNumber,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "保存しました", "data": printNumber}
