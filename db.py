import cfg
from sqlalchemy import create_engine

def create_sql_engine():
    connetion_url = 'postgresql://{user}:{password}@{host}:{port}/{db}'.format(
        user=cfg.DB_USER, password=cfg.DB_PASSWORD, host=cfg.DB_HOST, port=cfg.DB_PORT, db=cfg.DB_NAME)
    return create_engine(connetion_url)

# Create buyer
def create_buyer(buyer_id):
    engine = create_sql_engine()
    r = engine.execute('INSERT INTO buyer (buyer_id) values ({buyer_id})'.format(buyer_id=buyer_id))
    engine.dispose()


def create_seller(seller_id, seller_name):
    engine = create_sql_engine()
    r = engine.execute('INSERT INTO seller (seller_id, seller_name) values ({seller_id}, \'{seller_name}\')'.format(
        seller_id=seller_id, seller_name=seller_name))
    engine.dispose()


if __name__ == '__main__':
    create_buyer(26)
    create_seller(22, 'Nic Company')

# create seller

# create seller location ( as connected to seller)


