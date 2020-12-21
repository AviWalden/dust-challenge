SET search_path='public';
CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;

CREATE OR REPLACE FUNCTION public.update_last_modified() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
    BEGIN
        OLD.last_modified := NOW();
        RETURN NEW;
    END;
$$;

CREATE TABLE customer_data (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  title TEXT,
  company TEXT,
  catalog TEXT,
  create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  last_modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
  active BOOLEAN,
  image_url text
);
