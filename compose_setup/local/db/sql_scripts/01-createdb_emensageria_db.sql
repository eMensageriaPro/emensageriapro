-- Role: emensageriapro

-- DROP ROLE emensageriapro;

CREATE ROLE emensageriapro LOGIN
  PASSWORD 'debug1234'
  NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;

-- Database: emensageriapro_db

-- DROP DATABASE emensageriapro_db;

CREATE DATABASE emensageriapro_db
  WITH OWNER = emensageriapro
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'pt_BR.UTF-8'
       LC_CTYPE = 'pt_BR.UTF-8'
       CONNECTION LIMIT = -1;