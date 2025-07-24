import os
import glob
import csv
import sys

def txt_to_csv_folder(input_folder='text', output_folder='csv'):
    """
    Chuyển tất cả file .txt trong thư mục input_folder thành .csv và lưu vào thư mục output_folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    for txt_path in glob.glob(os.path.join(input_folder, '*.txt')):
        name = os.path.splitext(os.path.basename(txt_path))[0]
        csv_path = os.path.join(output_folder, f'{name}.csv')
        with open(txt_path, 'r', encoding='utf-8') as f_in, \
             open(csv_path, 'w', encoding='utf-8', newline='') as f_out:
            writer = csv.writer(f_out)
            writer.writerow(['key', 'value'])
            for line in f_in:
                line = line.strip()
                if not line or line.startswith('##'):
                    continue
                if '=' in line:
                    key, value = line.split('=', 1)
                    writer.writerow([key, value])

def csv_to_txt_folder(input_folder='csv', output_folder='text_out'):
    """
    Chuyển tất cả file .csv trong thư mục input_folder thành .txt và lưu vào thư mục output_folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    for csv_path in glob.glob(os.path.join(input_folder, '*.csv')):
        name = os.path.splitext(os.path.basename(csv_path))[0]
        txt_path = os.path.join(output_folder, f'{name}.txt')
        with open(csv_path, 'r', encoding='utf-8') as f_in, \
             open(txt_path, 'w', encoding='utf-8') as f_out:
            reader = csv.DictReader(f_in)
            for row in reader:
                f_out.write(f"{row['key']}={row['value']}\n")

def print_usage():
    print("Usage: python convert.py [txt2csv|csv2txt|both]")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    mode = sys.argv[1].lower()
    if mode == 'txt2csv':
        # TXT -> CSV vào thư mục 'csv'
        txt_to_csv_folder(input_folder='text', output_folder='csv')
        print("Đã chuyển TXT → CSV vào thư mục 'csv/'.")
    elif mode == 'csv2txt':
        # CSV -> TXT vào thư mục 'text_out' (hoặc folder khác)
        csv_to_txt_folder(input_folder='csv', output_folder='text_out')
        print("Đã chuyển CSV → TXT vào thư mục 'text_out/'.")
    elif mode == 'both':
        txt_to_csv_folder(input_folder='text', output_folder='csv')
        csv_to_txt_folder(input_folder='csv', output_folder='text_out')
        print("Đã chuyển TXT → CSV vào 'csv/' và CSV → TXT vào 'text_out/'.")
    else:
        print_usage()
