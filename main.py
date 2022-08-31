import os

print("請輸入您要轉換的檔案類型(例如 '.py' '.txt')")
type=input('')
print('請輸入要替換掉的文字')
replace=input('')
print('請輸入要替換出的文字')
new=input('')
for filename in os.listdir('./files'):
    if filename.endswith(type):
        with open(f'files/{filename}','r',encoding='utf-8') as file:
            data=file.read()
            content = data.replace(replace,new)
        with open(f'files/{filename}','w',encoding='utf-8') as file:
            file.write(content)
        print(f'已替換 {filename}')
print('已全部替換完畢')