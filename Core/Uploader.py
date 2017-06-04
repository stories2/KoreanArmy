import pymysql

def UploadDataManager(crawledData):
    databaseConnection = pymysql.connect(host='stories3.iptime.org', user='KoreanArmy', password='toortoor%^%',
                       db='KoreanArmy', charset='utf8')

    for indexOfCrawledData in crawledData:
        uploadCursor = databaseConnection.cursor()
        print indexOfCrawledData
        try:
            sqlQuery = "insert into NoticeData values (" + indexOfCrawledData[0] + ", '" + indexOfCrawledData[1] \
                       + "', '" + indexOfCrawledData[2] + "', '" + indexOfCrawledData[3] + "', '" + indexOfCrawledData[4] + "');"
            print sqlQuery
            uploadCursor.execute(sqlQuery)
            databaseConnection.commit()
            print "Result: ok"
        except:
            databaseConnection.rollback()
            print "Result: fail"

    databaseConnection.close()
