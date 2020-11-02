-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Mario Castro
-- Caption:       Ultima Version
-- Project:       Sistema Nomina OSJ Carabobo
-- Changed:       2012-04-13 09:36
-- Created:       2012-03-21 10:06
PRAGMA foreign_keys = ON;

-- Schema: nomina_osjc
BEGIN;
CREATE TABLE admin(
  idadmin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK(idadmin>=0),
  loginadmin VARCHAR(45) NOT NULL,
  passadmin VARCHAR(45) NOT NULL
);
CREATE TABLE profesor(
  idprofesor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK(idprofesor>=0),
  nombreprofesor VARCHAR(100) NOT NULL,
  apellidoprofesor VARCHAR(100) NOT NULL,
  ciprofesor VARCHAR(8) NOT NULL,
  nucleoprofesor VARCHAR(100) NOT NULL,
  telefonoprofesor VARCHAR(100) NOT NULL,
  activoprofesor VARCHAR(2) NOT NULL
);
CREATE TABLE catedra(
  idcatedra INTEGER PRIMARY KEY NOT NULL CHECK(idcatedra>=0),
  nombrecatedra VARCHAR(100) NOT NULL
);
CREATE TABLE dias(
  lunes VARCHAR(2) NOT NULL,
  martes VARCHAR(2) NOT NULL,
  miercoles VARCHAR(2) NOT NULL,
  jueves VARCHAR(2) NOT NULL,
  viernes VARCHAR(2) NOT NULL,
  sabados VARCHAR(2) NOT NULL,
  profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0),
  FOREIGN KEY(profesor_idprofesor)
    REFERENCES profesor(idprofesor)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX diasprofid ON dias(profesor_idprofesor);

CREATE TABLE horas(
  horaentrada TIME,
  horasalida TIME,
  profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0),
  FOREIGN KEY(profesor_idprofesor)
    REFERENCES profesor(idprofesor)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX horasprofid ON horas(profesor_idprofesor);

CREATE TABLE asistencia(
  horasasistenciaprofesor INTEGER NOT NULL,
  fechaasistencia DATE NOT NULL,
  horaentradaasistencia TIME NOT NULL,
  horasalidaasistencia TIME NOT NULL,
  profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0),
  catedra_idcatedra INTEGER NOT NULL CHECK(catedra_idcatedra>=0),
  observaciones VARCHAR(100),
  FOREIGN KEY(profesor_idprofesor)
    REFERENCES profesor(idprofesor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY(catedra_idcatedra)
    REFERENCES catedra(idcatedra)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
);
CREATE INDEX asisprofid ON asistencia(profesor_idprofesor);
CREATE INDEX asiscatid ON asistencia(catedra_idcatedra);

CREATE TABLE profesor_has_catedra(
  profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0),
  catedra_idcatedra INTEGER NOT NULL CHECK(catedra_idcatedra>=0),
  FOREIGN KEY(profesor_idprofesor)
    REFERENCES profesor(idprofesor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY(catedra_idcatedra)
    REFERENCES catedra(idcatedra)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX hascatedraprofid ON profesor_has_catedra(catedra_idcatedra);
CREATE INDEX hascatedracatid ON profesor_has_catedra(profesor_idprofesor);
COMMIT;
