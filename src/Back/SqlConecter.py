import mysql.connector

# SQLコネクタクラス
class SqlConecter:
    def get_connection():
        return mysql.connector.connect(
            host="設定したホスト名",
            user="設定したユーザー名",
            password="設定したパスワード",
            database="設定したデータベース名"
        )
