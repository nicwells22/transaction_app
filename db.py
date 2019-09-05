import cfg
from sqlalchemy import create_engine
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


def create_transcation():



def create_item(item_id, transaction_id, item_name, item_common_name, item_cost):
    engine = create_sql_engine()
    r = engine.execute('''INSERT INTO items (item_id, transaction_id, item_name, item_common_name, item_cost)
                            VALUES ({id}, {transact_id}, {name}, {common_name}, {cost})
                            '''.format(id=item_id, transact_id=transaction_id, name=item_name, common_name=item_common_name, cost=item_cost))
    engine.dispose()


if __name__ == '__main__':
    r = random.randint(100, 10000)
    b = r
    s = r + 1
    sl1 = r + 2
    sl2 = r + 3

    create_buyer(b)
    create_seller(s, 'Nic Company')
    create_seller_location(sl1, s)
    create_seller_location(sl2, s, 33.33, 44.44)

# create seller

# create seller location ( as connected to seller)


