#!/bin/bash

echo "자동 백업 시작..."

git add .
git commit -m "Auto backup: $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main

echo "백업 완료!"
