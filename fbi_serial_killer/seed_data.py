import os
import sys
import django
from datetime import date

# 顯式添加專案根目錄到sys.path
sys.path.append('/Users/kalpakjian/Library/CloudStorage/Dropbox/homework/fbi_project')

# 設置Django環境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fbi_project.settings')
django.setup()

from fbi_serial_killer.models import FBI_Agent, Serial_Killer, Capture

def seed_data():
    # 清空所有資料
    Capture.objects.all().delete()
    Serial_Killer.objects.all().delete()
    FBI_Agent.objects.all().delete()

    # 生成FBI探員資料
    fbi_agents = [
        {"name": "約翰·道格拉斯", "badge_number": "FBI001", "join_year": 1970, "specialization": "犯罪心理剖繪"},
        {"name": "羅伯特·雷斯勒", "badge_number": "FBI002", "join_year": 1970, "specialization": "連環殺手側寫"},
        {"name": "溫蒂·卡爾", "badge_number": "FBI003", "join_year": 1977, "specialization": "心理學分析"},
        {"name": "比爾·坦奇", "badge_number": "FBI004", "join_year": 1965, "specialization": "行為科學"},
        {"name": "詹姆斯·霍蘭德", "badge_number": "FBI005", "join_year": 1980, "specialization": "暴力犯罪調查"},
        {"name": "克里斯蒂·帕拉佐洛", "badge_number": "FBI006", "join_year": 1990, "specialization": "犯罪分析"},
        {"name": "李察·羅傑斯", "badge_number": "FBI007", "join_year": 1985, "specialization": "人質救援"},
        {"name": "傑夫·賈馬爾", "badge_number": "FBI008", "join_year": 1980, "specialization": "現場指揮"},
        {"name": "珍妮特·雷諾", "badge_number": "FBI009", "join_year": 1975, "specialization": "司法管理"},
        {"name": "湯瑪斯·霍爾登", "badge_number": "FBI010", "join_year": 1960, "specialization": "情報分析"},
        {"name": "艾倫·帕克", "badge_number": "FBI011", "join_year": 1995, "specialization": "犯罪現場調查"},
        {"name": "瑪麗·陳", "badge_number": "FBI012", "join_year": 1988, "specialization": "數位鑑識"},
        {"name": "史蒂文·王", "badge_number": "FBI013", "join_year": 1992, "specialization": "心理戰術"},
        {"name": "麗莎·布朗", "badge_number": "FBI014", "join_year": 1983, "specialization": "被害人分析"},
        {"name": "大衛·李", "badge_number": "FBI015", "join_year": 1978, "specialization": "跨州追捕"},
        {"name": "蘇珊·張", "badge_number": "FBI016", "join_year": 1990, "specialization": "犯罪模式分析"},
        {"name": "詹姆斯·吳", "badge_number": "FBI017", "join_year": 1985, "specialization": "情報蒐集"},
        {"name": "凱倫·林", "badge_number": "FBI018", "join_year": 1993, "specialization": "談判專家"},
        {"name": "麥克·黃", "badge_number": "FBI019", "join_year": 1987, "specialization": "行動策劃"},
        {"name": "珍妮·蔡", "badge_number": "FBI020", "join_year": 1991, "specialization": "證據分析"},
        {"name": "艾瑞克·金", "badge_number": "FBI021", "join_year": 1980, "specialization": "連環殺手追蹤"},
    ]

    # 插入探員並保存返回的物件
    fbi_agent_objects = [FBI_Agent(**agent) for agent in fbi_agents]
    FBI_Agent.objects.bulk_create(fbi_agent_objects)
    print(f"成功創建 {len(fbi_agent_objects)} 筆探員記錄！")

    # 刷新探員ID
    fbi_agents_db = list(FBI_Agent.objects.order_by('id')[:21])  # 獲取插入的探員物件

    # 生成連環殺手資料
    serial_killers = [
        {"name": "塞繆爾·利特爾", "alias": "麥克道爾", "crime_period_start": 1970, "crime_period_end": 2005, "victim_count": 93, "description": "美國史上最兇殞的連環殺手，受害者多為邊緣女性。"},
        {"name": "丹尼斯·雷德", "alias": "BTK殺手", "crime_period_start": 1974, "crime_period_end": 1991, "victim_count": 10, "description": "以綑綁、折磨、殺害方式犯案，2005年因軟盤線索被捕。"},
        {"name": "泰德·邦迪", "alias": "校園兇手", "crime_period_start": 1974, "crime_period_end": 1978, "victim_count": 30, "description": "以魅力外表誘騙年輕女性，震驚美國。"},
        {"name": "約翰·蓋西", "alias": "小丑殺手", "crime_period_start": 1972, "crime_period_end": 1978, "victim_count": 33, "description": "以小丑形象犯案，受害者多為年輕男性。"},
        {"name": "艾德·肯珀", "alias": "女學生兇手", "crime_period_start": 1964, "crime_period_end": 1973, "victim_count": 10, "description": "高智商兇手，殺害家人與女學生。"},
        {"name": "理查德·蔡斯", "alias": "吸血鬼殺手", "crime_period_start": 1977, "crime_period_end": 1978, "victim_count": 6, "description": "因妄想症殺人並飲血。"},
        {"name": "蓋瑞·雷吉威", "alias": "綠河殺手", "crime_period_start": 1982, "crime_period_end": 1998, "victim_count": 49, "description": "受害者多為性工作者，長期未被發現。"},
        {"name": "傑佛瑞·達默", "alias": "密爾沃基食人魔", "crime_period_start": 1978, "crime_period_end": 1991, "victim_count": 17, "description": "以食人行為震驚世人。"},
        {"name": "哈羅德·希普曼", "alias": "死亡醫生", "crime_period_start": 1975, "crime_period_end": 1998, "victim_count": 250, "description": "英國醫生，濫用藥物殺害患者。"},
        {"name": "查爾斯·曼森", "alias": "曼森家族", "crime_period_start": 1969, "crime_period_end": 1969, "victim_count": 7, "description": "邪教領袖，指使信徒犯案。"},
        {"name": "詹姆斯·霍姆斯", "alias": "無", "crime_period_start": 1990, "crime_period_end": 2000, "victim_count": 12, "description": "在多州犯案，目標隨機。"},
        {"name": "湯姆·布朗", "alias": "公路兇手", "crime_period_start": 1985, "crime_period_end": 1995, "victim_count": 15, "description": "沿高速公路殺害旅人。"},
        {"name": "艾倫·李", "alias": "夜行者", "crime_period_start": 1978, "crime_period_end": 1988, "victim_count": 9, "description": "夜間潛入民宅犯案。"},
        {"name": "羅伯特·漢森", "alias": "獵人兇手", "crime_period_start": 1971, "crime_period_end": 1983, "victim_count": 17, "description": "在阿拉斯加狩獵受害者。"},
        {"name": "威廉·瓊斯", "alias": "無", "crime_period_start": 1980, "crime_period_end": 1990, "victim_count": 8, "description": "以暴力手段殺害陌生人。"},
        {"name": "理查德·拉米雷茲", "alias": "夜間潛行者", "crime_period_start": 1984, "crime_period_end": 1985, "victim_count": 13, "description": "洛杉磯連環兇手，夜間襲擊。"},
        {"name": "安德魯·庫南南", "alias": "無", "crime_period_start": 1997, "crime_period_end": 1997, "victim_count": 5, "description": "殺害時尚設計師凡賽斯。"},
        {"name": "維克多·赫雷納", "alias": "無", "crime_period_start": 1970, "crime_period_end": 1980, "victim_count": 6, "description": "長期逃亡的搶匪與兇手。"},
        {"name": "萊斯利·羅格", "alias": "無", "crime_period_start": 1975, "crime_period_end": 1990, "victim_count": 7, "description": "因網路線索被捕。"},
        {"name": "韋恩·威廉斯", "alias": "亞特蘭大兇手", "crime_period_start": 1979, "crime_period_end": 1981, "victim_count": 29, "description": "亞特蘭大黑人男童兇案主嫌。"},
        {"name": "喬爾·里夫金", "alias": "無", "crime_period_start": 1989, "crime_period_end": 1993, "victim_count": 9, "description": "紐約連環兇手，受害者多為性工作者。"},
    ]

    # 插入連環殺手並保存返回的物件
    serial_killer_objects = [Serial_Killer(**killer) for killer in serial_killers]
    Serial_Killer.objects.bulk_create(serial_killer_objects)
    print(f"成功創建 {len(serial_killer_objects)} 筆連環殺手記錄！")

    # 刷新連環殺手ID
    serial_killers_db = list(Serial_Killer.objects.order_by('id')[:21])  # 獲取插入的連環殺手物件

    # 生成捉拿記錄
    captures = [
        {"agent_idx": 0, "serial_killer_idx": 0, "capture_date": date(2012, 9, 15), "location": "加利福尼亞州洛杉磯", "details": "塞繆爾·利特爾因DNA證據與毒品指控被捕，後確認為連環殺手。"},
        {"agent_idx": 1, "serial_killer_idx": 1, "capture_date": date(2005, 2, 25), "location": "堪薩斯州威奇托", "details": "丹尼斯·雷德（BTK殺手）因軟盤線索被FBI追蹤逮捕。"},
        {"agent_idx": 2, "serial_killer_idx": 2, "capture_date": date(1978, 2, 15), "location": "佛羅里達州彭薩科拉", "details": "泰德·邦迪因偷車被捕，後確認為連環兇手。"},
        {"agent_idx": 3, "serial_killer_idx": 3, "capture_date": date(1978, 12, 13), "location": "伊利諾州芝加哥", "details": "約翰·蓋西因性侵指控被調查，發現多起兇案。"},
        {"agent_idx": 4, "serial_killer_idx": 4, "capture_date": date(1973, 4, 22), "location": "加利福尼亞州聖克魯茲", "details": "艾德·肯珀自首後被捕，承認多起兇案。"},
        {"agent_idx": 5, "serial_killer_idx": 5, "capture_date": date(1978, 12, 29), "location": "加利福尼亞州沙加緬度", "details": "理查德·蔡斯因精神異常行為被捕。"},
        {"agent_idx": 6, "serial_killer_idx": 6, "capture_date": date(2001, 11, 7), "location": "華盛頓州西雅圖", "details": "蓋瑞·雷吉威（綠河殺手）因DNA證據被捕。"},
        {"agent_idx": 7, "serial_killer_idx": 7, "capture_date": date(1991, 7, 22), "location": "威斯康辛州密爾沃基", "details": "傑佛瑞·達默因受害者逃脫報警被捕。"},
        {"agent_idx": 8, "serial_killer_idx": 8, "capture_date": date(2000, 1, 13), "location": "英國曼徹斯特", "details": "哈羅德·希普曼因醫療記錄異常被調查。"},
        {"agent_idx": 9, "serial_killer_idx": 9, "capture_date": date(1969, 12, 1), "location": "加利福尼亞州洛杉磯", "details": "查爾斯·曼森因邪教活動被捕。"},
        {"agent_idx": 10, "serial_killer_idx": 10, "capture_date": date(2000, 6, 10), "location": "德克薩斯州休士頓", "details": "詹姆斯·霍姆斯因目擊者報案被捕。"},
        {"agent_idx": 11, "serial_killer_idx": 11, "capture_date": date(1995, 8, 20), "location": "內華達州拉斯維加斯", "details": "湯姆·布朗因交通違規被捕，後發現兇案線索。"},
        {"agent_idx": 12, "serial_killer_idx": 12, "capture_date": date(1988, 3, 15), "location": "加利福尼亞州舊金山", "details": "艾倫·李因竊盜被捕，後連結兇案。"},
        {"agent_idx": 13, "serial_killer_idx": 13, "capture_date": date(1983, 6, 24), "location": "阿拉斯加安克拉治", "details": "羅伯特·漢森因受害者逃脫報警被捕。"},
        {"agent_idx": 14, "serial_killer_idx": 14, "capture_date": date(1990, 11, 5), "location": "俄亥俄州克利夫蘭", "details": "威廉·瓊斯因匿名舉報被捕。"},
        {"agent_idx": 15, "serial_killer_idx": 15, "capture_date": date(1985, 8, 31), "location": "加利福尼亞州洛杉磯", "details": "理查德·拉米雷茲因群眾辨認被捕。"},
        {"agent_idx": 16, "serial_killer_idx": 16, "capture_date": date(1997, 7, 15), "location": "佛羅里達州邁阿密", "details": "安德魯·庫南南因槍擊事件被捕。"},
        {"agent_idx": 17, "serial_killer_idx": 17, "capture_date": date(1980, 5, 7), "location": "佛羅里達州坦帕", "details": "維克多·赫雷納因搶劫被捕，後發現兇案。"},
        {"agent_idx": 18, "serial_killer_idx": 18, "capture_date": date(1996, 5, 18), "location": "瓜地馬拉瓜地馬拉城", "details": "萊斯利·羅格在美國大使館自首。"},
        {"agent_idx": 19, "serial_killer_idx": 19, "capture_date": date(1981, 5, 31), "location": "喬治亞州亞特蘭大", "details": "韋恩·威廉斯因纖維證據被捕。"},
    ]

    # 使用插入的物件直接創建捉拿記錄
    capture_objects = []
    for capture in captures:
        try:
            agent = fbi_agents_db[capture["agent_idx"]]
            serial_killer = serial_killers_db[capture["serial_killer_idx"]]
            capture_objects.append(Capture(
                agent=agent,
                serial_killer=serial_killer,
                capture_date=capture["capture_date"],
                location=capture["location"],
                details=capture["details"]
            ))
        except IndexError:
            print(f"錯誤：索引超出範圍 - 探員索引 {capture['agent_idx']} 或連環殺手索引 {capture['serial_killer_idx']}")

    Capture.objects.bulk_create(capture_objects)
    print(f"成功創建 {len(capture_objects)} 筆捉拿記錄！")

if __name__ == "__main__":
    seed_data()