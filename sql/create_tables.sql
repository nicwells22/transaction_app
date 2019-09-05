CREATE TABLE seller (
	seller_id integer PRIMARY KEY,
	seller_name text
);

CREATE TABLE seller_location (
	location_id integer PRIMARY KEY,
	seller_id integer REFERENCES seller (seller_id),
	location_lat numeric,
	location_long numeric
);

CREATE TABLE buyer (
	buyer_id integer PRIMARY KEY
);

CREATE TABLE transact (
	transaction_id integer PRIMARY KEY,
	location_id integer REFERENCES seller_location (location_id),
	buyer_id integer REFERENCES buyer (buyer_id),
	sub_total numeric,
	tax numeric,
	total numeric,
	transaction_lat numeric,
	transaction_long numeric,
	transaction_datetime timestamp
);

CREATE TABLE items (
	item_id integer PRIMARY KEY,
	transaction_id integer REFERENCES transact (transaction_id),
	item_name text,
	item_common_name text,
	item_cost numeric
);