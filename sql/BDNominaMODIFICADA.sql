-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Personal
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2012-06-08 15:07
-- Created:       2012-03-21 10:06
PRAGMA foreign_keys = OFF;

-- Schema: nomina_osjc
BEGIN;
CREATE TABLE "admin"(
  "idadmin" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idadmin">=0),
  "loginadmin" VARCHAR(45) NOT NULL,
  "passadmin" VARCHAR(45) NOT NULL,
  "nombrenucleo" VARCHAR(45) NOT NULL,
  "entidadfederal" VARCHAR(45) NOT NULL,
  "municipio" VARCHAR(45) NOT NULL,
  "preguntaseg" VARCHAR(45) NOT NULL,
  "respuestaseg" VARCHAR(45) NOT NULL
);


CREATE TABLE "profesor"(
  "ciprofesor" VARCHAR(8) PRIMARY KEY NOT NULL,
  "nombreprofesor" VARCHAR(100) NOT NULL,
  "apellidoprofesor" VARCHAR(100) NOT NULL,
  "telefonoprofesor" VARCHAR(100) NOT NULL,
  "activoprofesor" VARCHAR(2) NOT NULL,
  "tipoprofesor" INTEGER NOT NULL,
  "fechanacimiento" DATE NOT NULL,
  "email" VARCHAR(100) NOT NULL,
  CONSTRAINT "ciprofesor_UNIQUE"
    UNIQUE("ciprofesor")
);


CREATE TABLE "catedra"(
  "idcatedra" INTEGER PRIMARY KEY NOT NULL CHECK("idcatedra">=0),
  "nombrecatedra" VARCHAR(45) NOT NULL
);


CREATE TABLE "dias"(
  "dia" VARCHAR(45) NOT NULL,
  "horaentradamanana" TIME NOT NULL,
  "horasalidamanana" TIME NOT NULL,
  "horaentradatarde" TIME NOT NULL,
  "horasalidatarde" TIME NOT NULL,
  "horasmanana" TIME NOT NULL,
  "horastarde" TIME NOT NULL,
  "horaslaborales" TIME NOT NULL,
  "observaciones" VARCHAR(200),
  "fechaingreso" DATE NOT NULL,
  "profesor_ciprofesor" VARCHAR(100) NOT NULL,
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  CONSTRAINT "fk_dias_profesor1"
    FOREIGN KEY("profesor_ciprofesor")
    REFERENCES "profesor"("ciprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT "fk_dias_catedra1"
    FOREIGN KEY("catedra_idcatedra")
    REFERENCES "catedra"("idcatedra")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "dias.fk_dias_profesor1" ON "dias"("profesor_ciprofesor");
CREATE INDEX "dias.fk_dias_catedra1" ON "dias"("catedra_idcatedra");


CREATE TABLE "asistencia"(
  "horasasistenciaprofesor" TIME NOT NULL,
  "fechaasistencia" DATE NOT NULL,
  "diaasistencia" VARCHAR(45) NOT NULL,
  "horaentradaasistencia" TIME NOT NULL,
  "horasalidaasistencia" TIME NOT NULL,
  "observaciones" VARCHAR(100),
  "profesor_ciprofesor" VARCHAR(100) NOT NULL,
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  CONSTRAINT "fk_asistencia_profesor"
    FOREIGN KEY("profesor_ciprofesor")
    REFERENCES "profesor"("ciprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT "fk_asistencia_catedra1"
    FOREIGN KEY("catedra_idcatedra")
    REFERENCES "catedra"("idcatedra")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "asistencia.fk_asistencia_profesor" ON "asistencia"("profesor_ciprofesor");
CREATE INDEX "asistencia.fk_asistencia_catedra1" ON "asistencia"("catedra_idcatedra");

COMMIT;
