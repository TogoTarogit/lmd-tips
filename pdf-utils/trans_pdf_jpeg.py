from pdf2image import convert_from_path

def convert_pdf_to_jpg():
    # ユーザーにPDFファイルのパスを入力させる
    pdf_path = input("Enter the path of the PDF file: ")

    # ユーザーに出力フォルダを入力させる
    output_folder = input("Enter the output folder: ")

    # PDFを画像に変換
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        # 画像を保存
        image.save(f'{output_folder}/output_{i}.jpg', 'JPEG')

# 関数を呼び出す
convert_pdf_to_jpg()