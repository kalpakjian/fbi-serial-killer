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
