import json  # import json module, json파일 SQL에 보내기
import pymysql

# with statement
conn = pymysql.connect(host='14.32.18.73', user='dev3', password='bit39', db='project', charset='utf8')
curs = conn.cursor()
st = 'insert into Sung values'
en = ""
with open('sung1.json', encoding="utf-8") as json_file:
    json_data = json.load(json_file)
    for i in range(0, len(json_data["position"])):
        sqls = json_data["position"][i]["sangcode"], json_data["position"][i]["dongcode"],json_data["position"][i]["gu"], \
               json_data["position"][i]["dong"], json_data["position"][i]["gil"], json_data["position"][i][
                   "2015income"], \
               json_data["position"][i]["2016income"], json_data["position"][i]["2017income"], \
               json_data["position"][i]["2018income"] \
            , json_data["position"][i]["2019income"], json_data["position"][i]["2020eincome"], json_data["position"][i][
                   "exsung"] \
            , json_data["position"][i]["exsungrank"], json_data["position"][i]["exsungscore"], \
               json_data["position"][i]["ytyincrease"] \
            , json_data["position"][i]["ytyincreaserank"], json_data["position"][i]["ytyincreasescore"], \
               json_data["position"][i]["fivesung"], \
               json_data["position"][i]["fivesungrank"],json_data["position"][i]["fivesungscore"],\
            json_data["position"][i]["totalscore"]
        sql = st + str(sqls) + en

        curs.execute(sql)
        conn.commit()


