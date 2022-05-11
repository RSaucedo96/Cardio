import mysql.connector
import constants as cons


class Item:
    def __init__(self, item_name: str, price: float, total_payments=0, payments_done=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert total_payments >= 0, f"Quantity {total_payments} is not greater or equal to zero!"
        assert payments_done >= 0, f"Quantity {payments_done} is not greater or equal to zero!"
        # Assign to self object
        self.item_name = item_name
        self.price = price
        self.tp = total_payments
        self.pd = payments_done

    @classmethod
    def instantiate_from_db(cls, user_name: str):
        cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
        cur_a = cnx.cursor(buffered=True)
        user_table = "SELECT * FROM %s "
        cur_a.execute(user_table, user_name)

        for item in cur_a:
            Item(
                name=item.get('nombre_compra'),
                price=float(item.get('precio_total')),
                total_payments=int(item.get('cuotas_total')),
                payments_done=int(item.get('cuotas_pagadas'))
            )

        cur_a.close()
        cnx.close()

    @classmethod
    def update_to_db(cls, data_item: dict):
        cnx = mysql.connector.connect(user=cons.DBUSER,
                                      password=cons.DBPW,
                                      host=cons.DBHOST,
                                      database=cons.DBNAME)
        cur_a = cnx.cursor(buffered=True)
        add_item = ("INSERT INTO %s "
                    "(nombre_compra, precio_total, cuotas_total, cuotas_pagadas) "
                    "VALUES (%(nombre_compra)s, %(precio_total)s, %(cuotas_total)s, %(cuotas_pagadas)s)")
        cur_a.execute(add_item, data_item)
        cnx.commit()
        cur_a.close()
        cnx.close()
