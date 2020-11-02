CREATE TABLE admin(
  idadmin INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  loginadmin VARCHAR(45) NOT NULL,
  passadmin VARCHAR(45) NOT NULL
);

CREATE TABLE profesor(
  idprofesor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombreprofesor VARCHAR(100) NOT NULL,
  apellidoprofesor VARCHAR(100) NOT NULL,
  ciprofesor VARCHAR(8) NOT NULL,
  nucleoprofesor VARCHAR(100) NOT NULL,
  telefonoprofesor VARCHAR(100) NOT NULL,
  activoprofesor VARCHAR(2) NOT NULL
);

CREATE TABLE catedra(
  idcatedra INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombrecatedra VARCHAR(100) NOT NULL
);

CREATE TABLE dias(
  lunes VARCHAR(2) NOT NULL,
  martes VARCHAR(2) NOT NULL,
  miercoles VARCHAR(2) NOT NULL,
  jueves VARCHAR(2) NOT NULL,
  viernes VARCHAR(2) NOT NULL,
  sabados VARCHAR(2) NOT NULL,
  profesor_idprofesor INTEGER PRIMARY KEY NOT NULL,
  FOREIGN KEY(profesor_idprofesor) 
    REFERENCES profesor(idprofesor) 
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX diasprofid ON dias(profesor_idprofesor);

CREATE TABLE horas(
  horaentrada TIME,
  horasalida TIME,
  profesor_idprofesor INTEGER PRIMARY KEY NOT NULL,
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
  profesor_idprofesor INTEGER PRIMARY KEY NOT NULL,
  catedraasistencia VARCHAR(45) NOT NULL,
  observaciones VARCHAR(200),
  FOREIGN KEY(profesor_idprofesor)
    REFERENCES profesor(idprofesor)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX asisprofid ON asistencia(profesor_idprofesor);

CREATE TABLE profesor_has_catedra(
  profesor_idprofesor INTEGER NOT NULL,
  catedra_idcatedra INTEGER NOT NULL,
  PRIMARY KEY(profesor_idprofesor,catedra_idcatedra),
  FOREIGN KEY(profesor_idprofesor)
    REFERENCES profesor(idprofesor)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  FOREIGN KEY(catedra_idcatedra)
    REFERENCES catedra(idcatedra)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
CREATE INDEX hascatedraprofid ON profesor_has_catedra(profesor_idprofesor);
CREATE INDEX hascatedracatid ON profesor_has_catedra(profesor_idprofesor);