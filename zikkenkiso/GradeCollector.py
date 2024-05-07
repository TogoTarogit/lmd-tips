import os
import csv
import logging
from datetime import datetime

# 日付ごとのディレクトリとファイル名を設定
date_str = datetime.now().strftime("%Y-%m-%d")
log_directory = f"./logs/{date_str}"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# ログ設定
logging.basicConfig(
    filename=f'{log_directory}/program.log', 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_directories(path):
    """指定されたディレクトリ下の全てのディレクトリ名をリストとして返す。"""
    try:
        directories = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]
        logging.info(f"Found directories: {directories}")
        return directories
    except FileNotFoundError:
        logging.error(f"Error: The directory {path} does not exist.")
        return []
    except PermissionError:
        logging.error(f"Error: Permission denied to access {path}.")
        return []

def read_file(file_path):
    """ファイルを読み込み、内容を返す。"""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            logging.info(f"Successfully read file: {file_path}")
            return content
    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} does not exist.")
    except IOError:
        logging.error(f"Error: Cannot read the file {file_path}.")
    return ""

def parse_output(content,valid_exercises):
    """ファイルの内容から成績データを解析し，辞書形式で返す．"""
    
    exercises = {}
    lines = content.strip().split("\n")
    current_exercise = None
    add_next_line = False

    for line in lines:
        if add_next_line:
            exercises[current_exercise] = line.strip()[:5] # 5文字目までを取得
            add_next_line = False
        elif any(ex in line for ex in valid_exercises):
            current_exercise = line.strip().split()[0]
            add_next_line = True

    return exercises


def convert_grade(grade):
    """成績を指定された形式に変換する"""
    if 'Pass' in grade:
        return 1
    elif '***' in grade:
        return -1
    else:
        return 0

def save_to_csv(filename, data, headers):
    """データをCSVに保存する。"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student'] + headers)
        for student, grades in data.items():
            writer.writerow([student] + [grades.get(exercise, "N/A") for exercise in headers])
        logging.info(f"Data saved to {filename} successfully.")

def save_converted_grades(filename, data, headers):
    """成績を変換してCSVに保存する。"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Student'] + headers)
        for student, grades in data.items():
            writer.writerow([student] + [convert_grade(grades.get(exercise, "N/A")) for exercise in headers])
        logging.info(f"Converted grades saved to {filename} successfully.")

def main():
    parent_dir = "./seito"
    student_dirs = get_directories(parent_dir)
    all_exercises = set([
        'enshu_1_3', 'enshu_1_4', 'enshu_2_4', 'enshu_2_9',
        'enshu_3_3', 'enshu_3_8', 'enshu_4_5', 'enshu_4_6'
    ])
    student_grades = {}

    for student_dir in student_dirs:
        output_content = read_file(os.path.join(parent_dir, student_dir, 'output.txt'))
        grades = parse_output(output_content,all_exercises)
        student_grades[student_dir] = grades

    all_exercises = sorted(all_exercises)
    save_to_csv('grades.csv', student_grades, all_exercises)
    save_converted_grades('converted_grades.csv', student_grades, all_exercises)
    logging.info("Grades have been written to grades.csv and converted_grades.csv.")

if __name__ == '__main__':
    main()
