-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Personal
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2012-04-13 13:41
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
  "idprofesor" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idprofesor">=0),
  "nombreprofesor" VARCHAR(100) NOT NULL,
  "apellidoprofesor" VARCHAR(100) NOT NULL,
  "ciprofesor" VARCHAR(8) NOT NULL,
  "nucleoprofesor" VARCHAR(100) NOT NULL,
  "telefonoprofesor" VARCHAR(100) NOT NULL,
  "activoprofesor" VARCHAR(2) NOT NULL
);
CREATE TABLE "catedra"(
  "idcatedra" INTEGER PRIMARY KEY NOT NULL CHECK("idcatedra">=0),
  "nombrecatedra" VARCHAR(100) NOT NULL
);
CREATE TABLE "dias"(
  "lunes" VARCHAR(2) NOT NULL,
  "martes" VARCHAR(2) NOT NULL,
  "miercoles" VARCHAR(2) NOT NULL,
  "jueves" VARCHAR(2) NOT NULL,
  "viernes" VARCHAR(2) NOT NULL,
  "sabados" VARCHAR(2) NOT NULL,
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  FOREIGN KEY("catedra_idcatedra")
    REFERENCES "catedra"("idcatedra")
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY("profesor_idprofesor")
    REFERENCES "profesor"("idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "dias.fk_dias_catedra1" ON "dias"("catedra_idcatedra");
CREATE INDEX "dias.fk_dias_profesor1" ON "dias"("profesor_idprofesor");
CREATE TABLE "horas"(
  "horaentrada" TIME,
  "horasalida" TIME,
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  FOREIGN KEY("catedra_idcatedra")
    REFERENCES "catedra"("idcatedra")
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY("profesor_idprofesor")
    REFERENCES "profesor"("idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "horas.fk_horas_catedra1" ON "horas"("catedra_idcatedra");
CREATE INDEX "horas.fk_horas_profesor1" ON "horas"("profesor_idprofesor");
CREATE TABLE "asistencia"(
  "horasasistenciaprofesor" INTEGER NOT NULL,
  "fechaasistencia" DATE NOT NULL,
  "horaentradaasistencia" TIME NOT NULL,
  "horasalidaasistencia" TIME NOT NULL,
  "observaciones" VARCHAR(100),
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  FOREIGN KEY("catedra_idcatedra")
    REFERENCES "catedra"("idcatedra"),
  FOREIGN KEY("profesor_idprofesor")
    REFERENCES "profesor"("idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "asistencia.fk_asistencia_catedra1" ON "asistencia"("catedra_idcatedra");
CREATE INDEX "asistencia.fk_asistencia_profesor1" ON "asistencia"("profesor_idprofesor");
CREATE TABLE "profesor_has_catedra"(
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0),
  FOREIGN KEY("profesor_idprofesor")
    REFERENCES "profesor"("idprofesor")
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY("catedra_idcatedra")
    REFERENCES "catedra"("idcatedra")
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX "profesor_has_catedra.fk_profesor_has_catedra_profesor1" ON "profesor_has_catedra"("profesor_idprofesor");
CREATE INDEX "profesor_has_catedra.fk_profesor_has_catedra_catedra1" ON "profesor_has_catedra"("catedra_idcatedra");
COMMIT;
