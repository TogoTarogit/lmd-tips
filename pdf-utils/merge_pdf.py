import PyPDF2
import os
from pathlib import Path

def usage_and_notes():
    print("【使い方】")
    print("1. このプログラムを実行すると、結合したいPDFファイルがあるディレクトリを指定します。")
    print("2. 指定ディレクトリ下のPDFファイルが作成日時順に表示されます。")
    print("3. 結合するかどうかを選択します。yを入力すると結合が開始され、nを入力すると終了します。")
    print("4. 結合したPDFは指定ディレクトリ内のoutputディレクトリに保存されます。")
    print()
    print("【注意点】")
    print("- 指定ディレクトリ下に同名のoutputディレクトリが存在する場合、新たに作成されません。")
    print("- PDFファイルの結合順序は作成日時は名前順と選択可能です")
    print("- PyPDF2ライブラリが必要です。未インストールの場合は、pip install PyPDF2でインストールしてください。")
    print("----------------------------------------------------------------------")

def get_pdf_files_by_creation_time(directory):
    pdf_files = [str(file) for file in Path(directory).rglob('*.pdf')]
    pdf_files.sort(key=lambda x: os.path.getctime(x))
    return pdf_files

def get_pdf_files_by_name(directory):
    pdf_files = [str(file) for file in Path(directory).rglob('*.pdf')]
    pdf_files.sort(key=lambda x: os.path.basename(x))
    return pdf_files

def merge_pdfs(directory, pdf_files):
    # outputディレクトリを作成する．すでに存在する場合は何もしない
    output_dir = os.path.join(directory, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # PDFファイルを結合するためのオブジェクトを作成
    pdf_writer = PyPDF2.PdfWriter()  # この行を修正

    # 各PDFファイルを読み込み，結合オブジェクトに追加する
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    # 結合したPDFファイルをoutputディレクトリに出力
    output_pdf_path = os.path.join(output_dir, 'output.pdf')
    with open(output_pdf_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    return output_pdf_path

#########################
#main
#########################
def main():
    # 使い方と注意点を表示
    usage_and_notes()

    directory = input('指定ディレクトリを入力してください: ')
    directory = os.path.abspath(directory)
    print('指定ディレクトリの絶対パス:', directory)

    sort_choice = input('PDFファイルの取得方法を選択してください (1: 作成日時順, 2: 名前順): ')
    if sort_choice == '1':
        pdf_files = get_pdf_files_by_creation_time(directory)
        print('発見したPDFファイル名を作成日時順で出力する:')
    elif sort_choice == '2':
        pdf_files = get_pdf_files_by_name(directory)
        print('発見したPDFファイル名を名前順で出力する:')
    else:
        print('無効な選択です。終了します。')
        return

    for pdf_file in pdf_files:
        print(pdf_file)

    merge_choice = input('結合してよろしいですか? (y/n): ')
    if merge_choice.lower() == 'y':
        print('PDFを選択した順序で結合する')
        merged_pdf_path = merge_pdfs(directory, pdf_files)
        print('結合したファイルを出力するためのディレクトリ:', merged_pdf_path)
        print('結合したファイルの順でファイル名を出力する:')
        for pdf_file in pdf_files:
            print(pdf_file)
    else:
        print('結合せずに終了しました')

if __name__ == "__main__":
    main()