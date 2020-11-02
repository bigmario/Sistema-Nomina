-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Personal
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2012-03-30 10:30
-- Created:       2012-03-21 10:06
PRAGMA foreign_keys = ON;
PRAGMA encoding = "UTF-8";

-- Schema: nomina_osjc
BEGIN;
CREATE TABLE admin(
  idadmin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idadmin">=0),
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
  activoprofesor VARCHAR(2) NOT NULL,
  FOREIGN KEY catedra_idcatedra INTEGER NOT NULL CHECK(catedra_idcatedra>=0) REFERENCES catedra(idcatedra) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);
CREATE INDEX 

CREATE TABLE catedra(
  idcatedra INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK(idcatedra>=0),
  nombrecatedra VARCHAR(100) NOT NULL,
  FOREIGN KEY profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0) REFERENCES profesor(idprofesor)
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE dias(
  iddias INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK(iddias>=0),
  lunes VARCHAR(2) NOT NULL,
  martes VARCHAR(2) NOT NULL,
  miercoles VARCHAR(2) NOT NULL,
  jueves VARCHAR(2) NOT NULL,
  viernes VARCHAR(2) NOT NULL,
  sabado VARCHAR(2) NOT NULL,
  FOREIGN KEY profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0) REFERENCES profesor(idprofesor)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  FOREIGN KEY profesor_catedra_idcatedra INTEGER NOT NULL CHECK(profesor_catedra_idcatedra>=0) REFERENCES catedra(idcatedra) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE horas(
  idhoras INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK(idhoras>=0),
  horaentrada TIME,
  horasalida TIME,
  FOREIGN KEY profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0) REFERENCES profesor(idprofesor)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  FOREIGN KEY profesor_catedra_idcatedra INTEGER NOT NULL CHECK(profesor_catedra_idcatedra>=0) REFERENCES catedra(idcatedra) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

CREATE TABLE asistencia(
  idasistencia INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK(idasistencia>=0),
  horasasistenciaprofesor INTEGER NOT NULL,
  fechaasistencia DATE NOT NULL,
  horaentradaasistencia TIME NOT NULL,
  horasalidaasistencia TIME NOT NULL,
  FOREIGN KEY profesor_idprofesor INTEGER NOT NULL CHECK(profesor_idprofesor>=0) REFERENCES profesor(idprofesor)
      ON UPDATE CASCADE
      ON DELETE CASCADE,
  FOREIGN KEY profesor_catedra_idcatedra INTEGER NOT NULL CHECK(profesor_catedra_idcatedra>=0) REFERENCES catedra(idcatedra) 
      ON UPDATE CASCADE
      ON DELETE CASCADE
);

COMMIT;