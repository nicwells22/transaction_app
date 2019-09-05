import cfg
from sqlalchemy import create_engine
from datetime import datetime
import random

def create_sql_engine():
    connetion_url = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
        user=cfg.DB_USER, password=cfg.DB_PASSWORD, host=cfg.DB_HOST, port=cfg.DB_PORT, db=cfg.DB_NAME)
    return create_engine(connetion_url)

# Create buyer
def create_buyer(buyer_id):
    engine = create_sql_engine()
    r = engine.execute('INSERT INTO buyer (buyer_id) VALUES ({buyer_id})'.format(buyer_id=buyer_id))
    engine.dispose()


def create_seller(seller_id, seller_name):
    engine = create_sql_engine()
    r = engine.execute("INSERT INTO seller (seller_id, seller_name) VALUES ({seller_id}, '{seller_name}')".format(
        seller_id=seller_id, seller_name=seller_name))
    engine.dispose()


def create_seller_location(location_id, seller_id, location_lat=None, location_long=None):
    engine = create_sql_engine()
    location_lat = location_lat if location_lat else 'NULL'
    location_long = location_long if location_long else 'NULL'
    r = engine.execute('''INSERT INTO seller_location (location_id, seller_id, location_lat, location_long)
                            VALUES ({id}, {seller}, {lat}, {long})
                            '''.format(id=location_id, seller=seller_id, lat=location_lat, long=location_long))
    engine.dispose()


def create_transcation(transaction_id, location_id, buyer_id, sub_total, tax, total, transaction_lat=None, transaction_long=None):
    engine = create_sql_engine()
    transaction_lat = transaction_lat if transaction_lat else 'NULL'
    transaction_long = transaction_long if transaction_long else 'NULL'
    r = engine.execute('''INSERT INTO transact (transaction_id, location_id, buyer_id, sub_total, tax, total, transaction_datetime, transaction_lat, transaction_long)
                            VALUES ({id}, {location}, {buyer}, {sub_total}, {tax}, {total}, {time}, {lat}, {long})
                            '''.format(id=transaction_id, location=location_id, buyer=buyer_id, sub_total=sub_total, tax=tax, total=total, time='NOW()', lat=transaction_lat, long=transaction_long))
    engine.dispose()


def create_item(item_id, transaction_id, item_name, item_common_name, item_cost):
    engine = create_sql_engine()
    r = engine.execute('''INSERT INTO items (item_id, transaction_id, item_name, item_common_name, item_cost)
                            VALUES ({id}, {transact_id}, '{name}', '{common_name}', {cost})
                            '''.format(id=item_id, transact_id=transaction_id, name=item_name, common_name=item_common_name, cost=item_cost))
    engine.dispose()


if __name__ == '__main__':
    r = random.randint(100, 10000)
    b = r
    s = r + 1
    sl1 = r + 2
    sl2 = r + 3
    t = r + 4
    t2 = r + 5
    i = r + 6
    create_buyer(b)
    create_seller(s, 'Nic Company')
    create_seller_location(sl1, s)
    create_seller_location(sl2, s, 33.33, 44.44)
    create_transcation(t, sl1, b, 45.03, (45.03*0.07), 45.03 + (45.03*0.07), 55.55, -66.66)
    create_transcation(t2, sl1, b, 45.03, (45.03*0.07), 45.03 + (45.03*0.07))
    create_item(i, t, 'Golden Apple', 'Apple', 32)
    create_item(i + 1, t, 'Ripe Pineapple', 'Pineapple', 13.03)

# create seller

# create seller location ( as connected to seller)


