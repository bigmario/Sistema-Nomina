-- Creator:       MySQL Workbench 5.2.38/ExportSQLite plugin 2009.12.02
-- Author:        Personal
-- Caption:       New Model
-- Project:       Name of the project
-- Changed:       2012-03-30 10:30
-- Created:       2012-03-21 10:06
PRAGMA foreign_keys = OFF;
PRAGMA encoding = "UTF-8";

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
  "activoprofesor" VARCHAR(2) NOT NULL,
  "catedra_idcatedra" INTEGER NOT NULL CHECK("catedra_idcatedra">=0)
);

CREATE TABLE "catedra"(
  "idcatedra" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idcatedra">=0),
  "nombrecatedra" VARCHAR(100) NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0)
);

CREATE TABLE "dias"(
  "iddias" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("iddias">=0),
  "lunes" VARCHAR(2) NOT NULL,
  "martes" VARCHAR(2) NOT NULL,
  "miercoles" VARCHAR(2) NOT NULL,
  "jueves" VARCHAR(2) NOT NULL,
  "viernes" VARCHAR(2) NOT NULL,
  "sabado" VARCHAR(2) NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0)
);

CREATE TABLE "horas"(
  "idhoras" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idhoras">=0),
  "horaentrada" TIME,
  "horasalida" TIME,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0)
);

CREATE TABLE "asistencia"(
  "idasistencia" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idasistencia">=0),
  "horasasistenciaprofesor" INTEGER NOT NULL,
  "fechaasistencia" DATE NOT NULL,
  "horaentradaasistencia" TIME NOT NULL,
  "horasalidaasistencia" TIME NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0)
);


----------------
-------VISTAS
----------------

CREATE VIEW vista_profesor_catedra AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.activoprofesor pactivoprofesor, c.idcatedra cidcatedra, c.nombrecatedra cnombrecatedra, c.profesor_idprofesor cprofesor_idprofesor
    FROM profesor p, catedra c;

CREATE VIEW vista_catedra_profesor AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.activoprofesor pactivoprofesor, c.idcatedra cidcatedra, c.nombrecatedra cnombrecatedra, c.profesor_idprofesor cprofesor_idprofesor
    FROM profesor p, catedra c;

CREATE VIEW vista_profesor_asistencia AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.activoprofesor pactivoprofesor, a.idasistencia aidasistencia, a.horasasistenciaprofesor ahorasasistenciaprofesor, a.fechaasistencia afechaasistencia, a.horaentradaasistencia ahoraentradaasistencia, a.horasalidaasistencia ahorasalidaasistencia, a.profesor_idprofesor aprofesor_idprofesor, a.profesor_catedra_idcatedra aprofesor_catedra_idcatedra
    FROM profesor p, asistencia a;

CREATE VIEW vista_profesor_horas AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.activoprofesor pactivoprofesor, h.idhoras hidhoras, h.horaentrada hhoraentrada, h.horasalida hhorasalida, h.profesor_idprofesor hprofesor_idprofesor, h.profesor_catedra_idcatedra hprofesor_catedra_idcatedra
    FROM profesor p, horas h;

CREATE VIEW vista_profesor_dias AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.activoprofesor pactivoprofesor, d.iddias diddias, d.lunes dlunes, d.martes dmartes, d.miercoles dmiercoles, d.jueves djueves, d.viernes dviernes, d.sabado dsabado, d.profesor_idprofesor dprofesor_idprofesor, d.profesor_catedra_idcatedra dprofesor_catedra_idcatedra
    FROM profesor p, dias d;


----------------
-------TRIGGERS INSERT 
----------------

CREATE TRIGGER on_insert_vista_profesor_catedra
INSTEAD OF INSERT ON vista_profesor_catedra
FOR EACH ROW
BEGIN
    INSERT INTO profesor (pnombreprofesor, papellidoprofesor, pciprofesor, pnucleoprofesor, ptelefonoprofesor, pactivoprofesor, pcatedra_idcatedra) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.ptelefonoprofesor, NEW.pactivoprofesor, NEW.pcatedra_idcatedra);
    INSERT INTO catedra (cnombrecatedra, cprofesor_idprofesor) VALUES (NEW.cnombrecatedra, NEW.pidprofesor);
END;

CREATE TRIGGER on_insert_vista_catedra_profesor
INSTEAD OF INSERT ON vista_catedra_profesor
FOR EACH ROW
BEGIN
    INSERT INTO profesor (pnombreprofesor, papellidoprofesor, pciprofesor, pnucleoprofesor, ptelefonoprofesor, pactivoprofesor, pcatedra_idcatedra) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.ptelefonoprofesor, NEW.pactivoprofesor, NEW.pcatedra_idcatedra);
    INSERT INTO catedra (nombrecatedra, profesor_idprofesor) VALUES (NEW.cnombrecatedra, NEW.pidprofesor);
END;

CREATE TRIGGER on_insert_vista_profesor_asistencia
INSTEAD OF INSERT ON vista_profesor_asistencia
FOR EACH ROW
BEGIN
    INSERT INTO profesor (pnombreprofesor, papellidoprofesor, pciprofesor, pnucleoprofesor, ptelefonoprofesor, pactivoprofesor, pcatedra_idcatedra) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.ptelefonoprofesor, NEW.pactivoprofesor, NEW.pcatedra_idcatedra);
    INSERT INTO asistencia (horasasistenciaprofesor, fechaasistencia, horaentradaasistencia, horasalidaasistencia, profesor_idprofesor, profesor_catedra_idcatedra) VALUES (NEW.ahorasasistenciaprofesor, NEW.afechaasistencia, NEW.ahoraentradaasistencia, NEW.ahorasalidaasistencia, NEW.aprofesor_idprofesor, NEW.aprofesor_catedra_idcatedra);
END;

CREATE TRIGGER on_insert_vista_profesor_horas
INSTEAD OF INSERT ON vista_profesor_horas
FOR EACH ROW
BEGIN
    INSERT INTO profesor (pnombreprofesor, papellidoprofesor, pciprofesor, pnucleoprofesor, ptelefonoprofesor, pactivoprofesor, pcatedra_idcatedra) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.ptelefonoprofesor, NEW.pactivoprofesor, NEW.pcatedra_idcatedra);
    INSERT INTO horas (horaentrada, horasalida, profesor_idprofesor, profesor_catedra_idcatedra) VALUES (NEW.ahorasasistenciaprofesor, NEW.afechaasistencia, NEW.ahoraentradaasistencia, NEW.ahorasalidaasistencia, NEW.aprofesor_idprofesor, NEW.aprofesor_catedra_idcatedra);
END;

CREATE TRIGGER on_insert_vista_profesor_dias
INSTEAD OF INSERT ON vista_profesor_dias
FOR EACH ROW
BEGIN
    INSERT INTO profesor (pnombreprofesor, papellidoprofesor, pciprofesor, pnucleoprofesor, ptelefonoprofesor, pactivoprofesor, pcatedra_idcatedra) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.ptelefonoprofesor, NEW.pactivoprofesor, NEW.pcatedra_idcatedra);
    INSERT INTO dias (lunes, martes, miercoles, jueves, viernes, sabado, profesor_idprofesor, profesor_catedra_idcatedra) VALUES (NEW.dlunes, NEW.dmartes, NEW.dmiercoles, NEW.djueves, NEW.dviernes, NEW.dsabado, NEW.dprofesor_idprofesor, NEW.dprofesor_catedra_idcatedra);
END;


----------------
-------TRIGGERS UPDATE
----------------
CREATE TRIGGER on_update_vista_profesor_catedra
INSTEAD OF UPDATE ON vista_profesor_catedra
FOR EACH ROW
BEGIN
     UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, telefonoprofesor=NEW.ptelefonoprofesor, activoprofesor=NEW.pactivoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra WHERE idprofesor=NEW.pidprofesor
     UPDATE catedra SET nombrecatedra=NEW.cnombrecatedra, profesor_idprofesor=NEW.cprofesor_idprofesor WHERE idcatedra=NEW.cidcatedra
END;

CREATE TRIGGER on_update_vista_catedra_profesor
INSTEAD OF UPDATE ON vista_catedra_profesor
FOR EACH ROW
BEGIN
     UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, telefonoprofesor=NEW.ptelefonoprofesor, activoprofesor=NEW.pactivoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra WHERE idprofesor=NEW.pidprofesor
     UPDATE catedra SET nombrecatedra=NEW.cnombrecatedra, profesor_idprofesor=NEW.cprofesor_idprofesor WHERE idcatedra=NEW.cidcatedra
END;

CREATE TRIGGER on_update_vista_profesor_asistencia
INSTEAD OF UPDATE ON vista_profesor_asistencia
FOR EACH ROW
BEGIN
     UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, telefonoprofesor=NEW.ptelefonoprofesor, activoprofesor=NEW.pactivoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra WHERE idprofesor=NEW.pidprofesor
     UPDATE asistencia SET horasasistenciaprofesor=NEW.ahorasasistenciaprofesor, fechaasistencia=NEW.afechaasistencia, horaentradaasistencia=NEW.ahoraentradaasistencia, horasalidaasistencia=NEW.ahorasalidaasistencia, profesor_idprofesor=NEW.aprofesor_idprofesor, profesor_catedra_idcatedra=NEW.aprofesor_catedra_idcatedra WHERE idasistencia=NEW.aidasistencia
END;

CREATE TRIGGER on_update_vista_profesor_horas
INSTEAD OF UPDATE ON vista_profesor_horas
FOR EACH ROW
BEGIN
     UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, telefonoprofesor=NEW.ptelefonoprofesor, activoprofesor=NEW.pactivoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra WHERE idprofesor=NEW.pidprofesor
     UPDATE horas SET horaentrada=NEW.hhoraentrada, horasalida=NEW.hhorasalida, profesor_idprofesor=NEW.hprofesor_idprofesor, profesor_catedra_idcatedra=NEW.hprofesor_catedra_idcatedra WHERE idhoras=NEW.hidhoras
END;

CREATE TRIGGER on_update_vista_profesor_dias
INSTEAD OF UPDATE ON vista_profesor_dias
FOR EACH ROW
BEGIN
     UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, telefonoprofesor=NEW.ptelefonoprofesor, activoprofesor=NEW.pactivoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra WHERE idprofesor=NEW.pidprofesor
     UPDATE dias SET lunes=NEW.dlunes, martes=NEW.dmartes, miercoles=NEW.dmiercoles, jueves=NEW.djueves, viernes=NEW.dviernes, sabado=NEW.dsabado, profesor_idprofesor=NEW.dprofesor_idprofesor, profesor_catedra_idcatedra=NEW.dprofesor_catedra_idcatedra, WHERE iddias=NEW.diddias
END;

----------------
-------TRIGGERS DELETE
----------------

CREATE TRIGGER on_delete_vista_profesor_catedra
INSTEAD OF DELETE ON vista_profesor_catedra
FOR EACH ROW
BEGIN
     DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
     DELETE FROM catedra WHERE idcatedra=NEW.cidcatedra;
END;

CREATE TRIGGER on_delete_vista_catedra_profesor
INSTEAD OF DELETE ON vista_catedra_profesor
FOR EACH ROW
BEGIN
     DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
     DELETE FROM catedra WHERE idcatedra=NEW.cidcatedra;
END;

CREATE TRIGGER on_delete_vista_profesor_asistencia
INSTEAD OF DELETE ON vista_profesor_asistencia
FOR EACH ROW
BEGIN
     DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
     DELETE FROM asistencia WHERE idasistencia=NEW.aidasistencia;
END;

CREATE TRIGGER on_delete_vista_profesor_horas
INSTEAD OF DELETE ON vista_profesor_horas
FOR EACH ROW
BEGIN
     DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
     DELETE FROM horas WHERE idhoras=NEW.hidhoras;
END;

CREATE TRIGGER on_delete_vista_profesor_dias
INSTEAD OF DELETE ON vista_profesor_dias
FOR EACH ROW
BEGIN
     DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
     DELETE FROM dias WHERE iddias=NEW.diddias;
END;

COMMIT;