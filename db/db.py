import mysql.connector

class Database:
    def __init__(self):
        self.db=None

    def ulanish(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="foodservice",
            port="3308"
        )

    def ishlatish(self,sql,fetchall=False, fetchone=False, commit=False):
        self.db=self.ulanish()
        cursor=self.db.cursor()
        cursor.execute(sql)
        data=None
        if fetchall:
            data = cursor.fetchall()
        elif fetchone:
            data= cursor.fetchone()
        elif commit:
            self.db.commit()
        self.db.close()
        return data

    def foodlist(self):
        sql=f"select * from food"
        return self.ishlatish(sql, fetchall=True)
    def foodprice(self,id):
        sql=f"select min(narxi), max(narxi) from ovqat_miqdorlari where ovqat_id={id}"
        return self.ishlatish(sql, fetchone=True)

    def menudetail(self, id):
            sql=f""" SELECT ovqat_miqdorlari.narxi, 
            ovqat_miqdorlari.tarifi, 
            ovqat_miqdorlari.rasmi,
            miqdor.turi,
            ovqat_miqdorlari.id
            FROM miqdor INNER JOIN ovqat_miqdorlari 
            ON miqdor.id = ovqat_miqdorlari.miqdor_id 
            where ovqat_miqdorlari.ovqat_id={id}"""
            return self.ishlatish(sql, fetchall=True)

    def savatcha(self):
        sql="""
        SELECT food.nomi,
            ovqat_miqdorlari.narxi, 
            ovqat_miqdorlari.tarifi, 
            ovqat_miqdorlari.rasmi,
            miqdor.turi,
            savatcha.soni
        FROM miqdor
        INNER JOIN ovqat_miqdorlari ON miqdor.id = ovqat_miqdorlari.miqdor_id
        INNER JOIN savatcha ON ovqat_miqdorlari.id = savatcha.ovqat_id
        INNER JOIN food ON ovqat_miqdorlari.ovqat_id = food.id
        """
        return self.ishlatish(sql, fetchall=True)

    def zakazqushish(self,ism,fam,tel,

                     ):
        try:
            sql=f"""
            insert into zakazlar(ism, familiya,tel_raqam)
            values('{ism}', '{fam}','{tel}',')
            """
            self.ishlatish(sql , commit=True)
        except:
            print("xato bo'ldi")


obj=Database()
#a=obj.get_info()
#for i in a:
 #   print(*i)

