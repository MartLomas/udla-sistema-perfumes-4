CREATE TABLE "usuario" (
  "id_usuario" integer PRIMARY KEY NOT NULL,
  "username" varchar(32) NOT NULL,
  "password" varchar(256) NOT NULL,
  "estado" integer NOT NULL
);

CREATE TABLE "usuario_rol" (
  "id_usuario_rol" integer PRIMARY KEY NOT NULL,
  "id_usuario" integer NOT NULL,
  "id_rol" integer NOT NULL
);

CREATE TABLE "rol" (
  "id_rol" integer PRIMARY KEY NOT NULL,
  "nombre" varchar(32) NOT NULL,
  "estado" integer NOT NULL
);

CREATE TABLE "marcas" (
  "id_marca" integer PRIMARY KEY NOT NULL,
  "nombre" varchar(32) NOT NULL,
  "estado" integer NOT NULL
);

CREATE TABLE "genero" (
  "id_genero" integer PRIMARY KEY NOT NULL,
  "nombre" varchar(32) NOT NULL,
  "estado" integer NOT NULL
);

CREATE TABLE "aromas" (
  "id_aroma" integer PRIMARY KEY NOT NULL,
  "nombre" varchar(32) NOT NULL,
  "estado" integer NOT NULL
);

CREATE TABLE "perfumes" (
  "id_perfume" integer PRIMARY KEY NOT NULL,
  "nombre" varchar(50) NOT NULL,
  "id_marca" integer NOT NULL,
  "id_aroma" integer NOT NULL,
  "id_genero" integer NOT NULL,
  "tamanio" float NOT NULL,
  "precio" numeric(18,2) NOT NULL,
  "imagen" varchar(256),
  "estado" integer NOT NULL
);

COMMENT ON COLUMN "usuario"."id_usuario" IS 'Identificador único del usuario';
COMMENT ON COLUMN "usuario"."username" IS 'Nombre de usuario para login';
COMMENT ON COLUMN "usuario"."password" IS 'Contraseña cifrada del usuario';
COMMENT ON COLUMN "usuario"."estado" IS 'Estado del usuario (activo/inactivo)';
COMMENT ON COLUMN "usuario_rol"."id_usuario_rol" IS 'Identificador único del usuario-rol';
COMMENT ON COLUMN "usuario_rol"."id_usuario" IS 'Referencia al usuario';
COMMENT ON COLUMN "usuario_rol"."id_rol" IS 'Referencia al rol';
COMMENT ON COLUMN "rol"."id_rol" IS 'Identificador único del rol';
COMMENT ON COLUMN "rol"."nombre" IS 'Nombre del rol';
COMMENT ON COLUMN "rol"."estado" IS 'Estado del rol (activo/inactivo)';
COMMENT ON COLUMN "marcas"."id_marca" IS 'Identificador único de la marca';
COMMENT ON COLUMN "marcas"."nombre" IS 'Nombre de la marca';
COMMENT ON COLUMN "marcas"."estado" IS 'Estado de la marca (activo/inactivo)';
COMMENT ON COLUMN "genero"."id_genero" IS 'Identificador único del género';
COMMENT ON COLUMN "genero"."nombre" IS 'Nombre del género (masculino, femenino, unisex)';
COMMENT ON COLUMN "genero"."estado" IS 'Estado del género (activo/inactivo)';
COMMENT ON COLUMN "aromas"."id_aroma" IS 'Identificador único del aroma';
COMMENT ON COLUMN "aromas"."nombre" IS 'Nombre del aroma';
COMMENT ON COLUMN "aromas"."estado" IS 'Estado del aroma (activo/inactivo)';
COMMENT ON COLUMN "perfumes"."id_perfume" IS 'Identificador único del perfume';
COMMENT ON COLUMN "perfumes"."nombre" IS 'Nombre del perfume';
COMMENT ON COLUMN "perfumes"."id_marca" IS 'Referencia a la marca';
COMMENT ON COLUMN "perfumes"."id_aroma" IS 'Referencia al aroma';
COMMENT ON COLUMN "perfumes"."id_genero" IS 'Referencia al género';
COMMENT ON COLUMN "perfumes"."tamanio" IS 'Tamaño del perfume en mililitros';
COMMENT ON COLUMN "perfumes"."precio" IS 'Precio del perfume en dólares';
COMMENT ON COLUMN "perfumes"."imagen" IS 'URL de la imagen del perfume';
COMMENT ON COLUMN "perfumes"."estado" IS 'Estado del perfume (activo/inactivo)';

ALTER TABLE "usuario_rol" ADD FOREIGN KEY ("id_usuario") REFERENCES "usuario" ("id_usuario");
ALTER TABLE "usuario_rol" ADD FOREIGN KEY ("id_rol") REFERENCES "rol" ("id_rol");
ALTER TABLE "perfumes" ADD FOREIGN KEY ("id_marca") REFERENCES "marcas" ("id_marca");
ALTER TABLE "perfumes" ADD FOREIGN KEY ("id_aroma") REFERENCES "aromas" ("id_aroma");
ALTER TABLE "perfumes" ADD FOREIGN KEY ("id_genero") REFERENCES "genero" ("id_genero");

CREATE SEQUENCE aromas_id_seq START 1;
CREATE SEQUENCE genero_id_seq START 1;
CREATE SEQUENCE marcas_id_seq START 1;
CREATE SEQUENCE perfumes_id_seq START 1;

ALTER TABLE "aromas" ALTER COLUMN "id_aroma" SET DEFAULT nextval('aromas_id_seq');
ALTER TABLE "genero" ALTER COLUMN "id_genero" SET DEFAULT nextval('genero_id_seq');
ALTER TABLE "marcas" ALTER COLUMN "id_marca" SET DEFAULT nextval('marcas_id_seq');
ALTER TABLE "perfumes" ALTER COLUMN "id_perfume" SET DEFAULT nextval('perfumes_id_seq');

-- Init authentication data
INSERT INTO public.usuario
(id_usuario, username, "password", estado)
VALUES(1, 'admin', 'Passwrod01', 1);

INSERT INTO public.usuario
(id_usuario, username, "password", estado)
VALUES(2, 'consultor', 'Passwrod01', 1);

INSERT INTO public.rol
(id_rol, nombre, estado)
VALUES(1, 'ADMINISTRADOR', 1);

INSERT INTO public.rol
(id_rol, nombre, estado)
VALUES(2, 'CONSULTOR', 1);

INSERT INTO public.usuario_rol
(id_usuario_rol, id_usuario, id_rol)
VALUES(1, 1, 1);

INSERT INTO public.usuario_rol
(id_usuario_rol, id_usuario, id_rol)
VALUES(2, 2, 2);

-- Inicializar datos de aromas
INSERT INTO public.aromas
(id_aroma, nombre, estado)
VALUES(1, 'Amaderado', 1);

INSERT INTO public.aromas
(id_aroma, nombre, estado)
VALUES(2, 'Dulce', 1);

INSERT INTO public.aromas
(id_aroma, nombre, estado)
VALUES(3, 'Acido', 1);

-- Inicializar datos de géneros
INSERT INTO public.genero
(id_genero, nombre, estado)
VALUES(1, 'Masculino', 1);

INSERT INTO public.genero
(id_genero, nombre, estado)
VALUES(2, 'Femenino', 1);

-- Inicializar datos de marcas
INSERT INTO public.marcas
(id_marca, nombre, estado)
VALUES(1, 'Armani', 1);

INSERT INTO public.marcas
(id_marca, nombre, estado)
VALUES(3, 'Hugo Boss', 1);