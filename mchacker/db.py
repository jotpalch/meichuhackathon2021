import pymysql

def db_add(user_id="",access_token="") :

    db_settings = {
        "host": "phpmyadmin.exodus.tw",
        "port": 3306,
        "user": "jotp",
        "password": "123123123",
        "db": "jotp_DB",
        "charset": "utf8"
    }

    last_id = 1

    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            command = "SELECT id FROM user_token ORDER BY id DESC LIMIT 0 , 1"
            cursor.execute(command)
            result = cursor.fetchone()
            print(result)
            last_id = result[0] if result != None else 0

        with conn.cursor() as cursor:
            command = "INSERT INTO `user_token` (`id`, `user_id`, `token`) VALUES (%s, %s, %s);"
            cursor.execute(command, (str(last_id+1),user_id,access_token))
            print("add ",access_token," success")
            conn.commit()

    except Exception as ex:
        print(ex)
