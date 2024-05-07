#!/bin/bash
# run_output_for_a_day_with_logs.sh

# ログファイルのパスを設定
log_file="/path/to/your/log/directory/output_log_$(date +%Y%m%d%H%M%S).log"

# Pythonスクリプトのディレクトリへ移動
cd /path/to/your/script/directory

# 開始時刻を記録
start_time=$(date +%s)

# 86400秒 (24時間) でループを終了
while true
do
  # Pythonスクリプトを実行し、出力をログファイルに記録
  /usr/bin/python3 output.py >> "$log_file" 2>&1
  
  # 現在時刻と開始時刻の差を計算
  current_time=$(date +%s)
  elapsed_time=$((current_time - start_time))
  
  # 経過時間が24時間に達したらループを終了
  if [ $elapsed_time -ge 86400 ]; then
    break
  fi

  sleep 1800  # 1800秒（30分）待機
done
