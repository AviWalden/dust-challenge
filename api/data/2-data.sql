COPY customer_data(id,title,company,catalog,create_date,last_modified,active,image_url)
FROM '/docker-entrypoint-initdb.d/db.csv'
DELIMITER ','
CSV HEADER;
