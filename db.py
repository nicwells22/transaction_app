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
    print(r)

# if __name__ == '__main__':
#     create_buyer(22)

# create seller

# create seller location ( as connected to seller)


