# FBI Serial Killer Django Project

Django應用程式，模擬FBI追捕連環殺手的資料管理，包含探員、連環殺手和捉拿記錄。

## 功能
- 模型：FBI_Agent、Serial_Killer、Capture。
- 資料：21筆探員、21筆連環殺手、20筆捉拿記錄。
- 網頁：`http://127.0.0.1:8000/captures/`展示捉拿記錄。

## 運行
1. 克隆倉庫：
   ```bash
   git clone https://github.com/kalpakjian/fbi-serial-killer.git
   cd fbi-serial-killer

python3 manage.py migrate

python3 fbi_serial_killer/seed_data.py

python3 manage.py runserver

訪問http://127.0.0.1:8000/captures/

admin page: http://127.0.0.1:8000/admin/

##################

按照功課要求做以下動作，所需要指令

## 資料測試
1. 匯出資料：
   python3 manage.py dumpdata fbi_serial_killer --indent 2 > fbi_serial_killer/fixtures/data.json

2. 格式化資料集
dumpdata已使用--indent 2格式化，data.json應為可讀JSON。

3. 清理原始資料
python manage.py flush

4 .匯入資料：
python3 manage.py loaddata fbi_serial_killer/fixtures/data.json
驗證：訪問http://127.0.0.1:8000/captures/，應顯示20筆捉拿記錄。

   
