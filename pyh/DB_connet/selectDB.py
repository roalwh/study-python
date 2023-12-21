import pymysql

#접속정보
conn = pymysql.connect(
                host='roalwh.iptime.org',
                port=21356,
                user='ex',
                password='1234',
                db='mydb2',
                charset='utf8')

cur = conn.cursor()

# 사용할 SQL 문
sql = "SELECT * FROM drink"

# sql 실행
cur.execute(sql)
result = cur.fetchall()

# 출력
# for x in result:
#     print(x)
print("현재 데이터수는 총 {}개 입니다".format(len(result)))
print(result[100])
print("\n"+result[100][1],result[100][2],result[100][4],result[100][6])

# # 커밋
# conn.commit()

# 접속종료
conn.close()
