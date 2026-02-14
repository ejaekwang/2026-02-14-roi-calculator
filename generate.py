import json
import os
from datetime import datetime

# 1. 데이터 불러오기
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

investment = data["investment"]
monthly_profit = data["monthly_profit"]
device = data["device"]

# 2. ROI 계산
months = investment / monthly_profit

# 3. HTML 자동 생성
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>ROI Calculator</title>
</head>
<body>
    <h1>ROI 자동 계산기</h1>
    <h2>기기: {device}</h2>
    <p>총 투자금: {investment:,} 원</p>
    <p>월 수익: {monthly_profit:,} 원</p>
    <h3>회수 기간: {months:.1f} 개월</h3>
    <p>생성 시간: {datetime.now()}</p>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ HTML 생성 완료")

# 4. 자동 Git Push
os.system("git add .")
os.system('git commit -m "자동 업데이트"')
os.system("git push")

print("🚀 GitHub 자동 업로드 완료")
