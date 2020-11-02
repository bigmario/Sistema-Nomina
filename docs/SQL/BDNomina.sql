-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Personal
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2012-03-21 15:51
-- Created:       2012-03-21 10:06
PRAGMA foreign_keys = OFF;

-- Schema: nomina_osjc
BEGIN;
CREATE TABLE "admin"(
  "idadmin" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idadmin">=0),
  "loginadmin" VARCHAR(45) NOT NULL,
  "passadmin" VARCHAR(45) NOT NULL
);
CREATE TABLE "profesor"(
  "idprofesor" INTEGER CHECK("idprofesor">=0),
  "nombreprofesor" VARCHAR(100) NOT NULL,
  "apellidoprofesor" VARCHAR(100) NOT NULL,
  "ciprofesor" VARCHAR(8) NOT NULL,
  "nucleoprofesor" VARCHAR(100) NOT NULL,
  "catedraprofesor" INTEGER NOT NULL,
  "telefonoprofesor" VARCHAR(100) NOT NULL,
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  "catedra_profesor_idprofesor" INTEGER NOT NULL CHECK("catedra_profesor_idprofesor">=0),
  "activoprofesor" VARCHAR(2) NOT NULL,
  PRIMARY KEY("idprofesor","catedra_idcatedra","catedra_profesor_idprofesor"),
  CONSTRAINT "fk_profesor_catedra1"
    FOREIGN KEY("catedra_idcatedra","catedra_profesor_idprofesor")
    REFERENCES "catedra"("idcatedra","profesor_idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "profesor.fk_profesor_catedra1" ON "profesor"("catedra_idcatedra","catedra_profesor_idprofesor");
CREATE TABLE "catedra"(
  "idcatedra" INTEGER NOT NULL CHECK("idcatedra">=0),
  "nombrecatedra" VARCHAR(100) NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  PRIMARY KEY("idcatedra","profesor_idprofesor"),
  CONSTRAINT "fk_catedra_profesor"
    FOREIGN KEY("profesor_idprofesor")
    REFERENCES "profesor"("idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "catedra.fk_catedra_profesor" ON "catedra"("profesor_idprofesor");
CREATE TABLE "dias"(
  "iddias" INTEGER NOT NULL CHECK("iddias">=0),
  "lunes" VARCHAR(2) NOT NULL,
  "martes" VARCHAR(2) NOT NULL,
  "miercoles" VARCHAR(2) NOT NULL,
  "jueves" VARCHAR(2) NOT NULL,
  "viernes" VARCHAR(2) NOT NULL,
  "sabados" VARCHAR(2) NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0),
  "profesor_catedra_profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_catedra_profesor_idprofesor">=0),
  PRIMARY KEY("iddias","profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor"),
  CONSTRAINT "fk_dias_profesor1"
    FOREIGN KEY("profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor")
    REFERENCES "profesor"("idprofesor","catedra_idcatedra","catedra_profesor_idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "dias.fk_dias_profesor1" ON "dias"("profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor");
CREATE TABLE "horas"(
  "idhoras" INTEGER NOT NULL,
  "horaentrada" TIME,
  "horasalida" TIME,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0),
  "profesor_catedra_profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_catedra_profesor_idprofesor">=0),
  PRIMARY KEY("idhoras","profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor"),
  CONSTRAINT "fk_horas_profesor1"
    FOREIGN KEY("profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor")
    REFERENCES "profesor"("idprofesor","catedra_idcatedra","catedra_profesor_idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "horas.fk_horas_profesor1" ON "horas"("profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor");
CREATE TABLE "asistencia"(
  "idasistencia" INTEGER NOT NULL,
  "asistenciaprofesor" INTEGER NOT NULL,
  "fechaasistencia" DATE NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0),
  "profesor_catedra_profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_catedra_profesor_idprofesor">=0),
  PRIMARY KEY("idasistencia","profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor"),
  CONSTRAINT "fk_asistencia_profesor1"
    FOREIGN KEY("profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor")
    REFERENCES "profesor"("idprofesor","catedra_idcatedra","catedra_profesor_idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "asistencia.fk_asistencia_profesor1" ON "asistencia"("profesor_idprofesor","profesor_catedra_idcatedra","profesor_catedra_profesor_idprofesor");
COMMIT;
