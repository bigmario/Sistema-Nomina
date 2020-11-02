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
  "idprofesor" INTEGER NOT NULL CHECK("idprofesor">=0),
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
  "sabado" VARCHAR(2) NOT NULL,
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
  "horasasistenciaprofesor" INTEGER NOT NULL,
  "fechaasistencia" DATE NOT NULL,
  "horaentradaasistencia" TIME NOT NULL,
  "horasalidaasistencia" TIME NOT NULL,
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

----------------
-------VISTAS
----------------

CREATE VIEW vista_profesor_catedra AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.catedraprofesor pcatedraprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.catedra_profesor_idprofesor pcatedra_profesor_idprofesor, p.activoprofesor pactivoprofesor, c.idcatedra cidcatedra, c.nombrecatedra cnombrecatedra, c.profesor_idprofesor cprofesor_idprofesor
    FROM profesor p, catedra c;

CREATE VIEW vista_catedra_profesor AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.catedraprofesor pcatedraprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.catedra_profesor_idprofesor pcatedra_profesor_idprofesor, p.activoprofesor pactivoprofesor, c.idcatedra cidcatedra, c.nombrecatedra cnombrecatedra, c.profesor_idprofesor cprofesor_idprofesor
    FROM profesor p, catedra c;

CREATE VIEW vista_profesor_asistencia AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.catedraprofesor pcatedraprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.catedra_profesor_idprofesor pcatedra_profesor_idprofesor, p.activoprofesor pactivoprofesor, a.idasistencia aidasistencia, a.horasasistenciaprofesor ahorasasistenciaprofesor, a.fechaasistencia afechaasistencia, a.horaentradaasistencia ahoraentradaasistencia, a.horasalidaasistencia ahorasalidaasistencia, a.profesor_idprofesor aprofesor_idprofesor, a.profesor_catedra_idcatedra aprofesor_catedra_idcatedra, a.profesor_catedra_profesor_idprofesor aprofesor_catedra_profesor_idprofesor
    FROM profesor p, asistencia a;

CREATE VIEW vista_profesor_horas AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.catedraprofesor pcatedraprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.catedra_profesor_idprofesor pcatedra_profesor_idprofesor, p.activoprofesor pactivoprofesor, h.idhoras hidhoras, h.horaentrada hhoraentrada, h.horasalida hhorasalida, h.profesor_idprofesor hprofesor_idprofesor, h.profesor_catedra_idcatedra hprofesor_catedra_idcatedra, h.profesor_catedra_profesor_idprofesor hprofesor_catedra_profesor_idprofesor
    FROM profesor p, horas h;

CREATE VIEW vista_profesor_dias AS
    SELECT p.idprofesor pidprofesor, p.nombreprofesor pnombreprofesor, p.apellidoprofesor papellidoprofesor, p.ciprofesor pciprofesor, p.nucleoprofesor pnucleoprofesor, p.catedraprofesor pcatedraprofesor, p.telefonoprofesor ptelefonoprofesor, p.catedra_idcatedra pcatedra_idcatedra, p.catedra_profesor_idprofesor pcatedra_profesor_idprofesor, p.activoprofesor pactivoprofesor, d.iddias diddias, d.lunes dlunes, d.martes dmartes, d.miercoles dmiercoles, d.jueves djueves, d.viernes dviernes, d.sabado dsabado, d.profesor_idprofesor dprofesor_idprofesor, d.profesor_catedra_idcatedra dprofesor_catedra_idcatedra, d.profesor_catedra_profesor_idprofesor dprofesor_catedra_profesor_idprofesor
    FROM profesor p, dias d;


----------------
-------TRIGGERS INSERT 
----------------

CREATE TRIGGER on_insert_vista_profesor_catedra
INSTEAD OF INSERT ON vista_profesor_catedra
FOR EACH ROW
BEGIN
    INSERT INTO profesor (pnombreprofesor, papellidoprofesor, pciprofesor, pnucleoprofesor, pcatedraprofesor, ptelefonoprofesor, pcatedra_idcatedra, pcatedra_profesor_idprofesor, pactivoprofesor) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.pcatedraprofesor, NEW.ptelefonoprofesor, NEW.pcatedra_idcatedra, NEW.pcatedra_profesor_idprofesor, NEW.pactivoprofesor);
    INSERT INTO catedra (cnombrecatedra, cprofesor_idprofesor) VALUES (NEW.cnombrecatedra, NEW.cprofesor_idprofesor);
END;

CREATE TRIGGER on_insert_vista_catedra_profesor
INSTEAD OF INSERT ON vista_catedra_profesor
FOR EACH ROW
BEGIN
    INSERT INTO profesor (nombreprofesor, apellidoprofesor, ciprofesor, nucleoprofesor, catedraprofesor, telefonoprofesor, catedra_idcatedra, catedra_profesor_idprofesor, activoprofesor) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.pcatedraprofesor, NEW.ptelefonoprofesor, NEW.pcatedra_idcatedra, NEW.pcatedra_profesor_idprofesor, NEW.pactivoprofesor);
    INSERT INTO catedra (nombrecatedra, profesor_idprofesor) VALUES (NEW.cnombrecatedra, NEW.cprofesor_idprofesor);
END;

CREATE TRIGGER on_insert_vista_profesor_asistencia
INSTEAD OF INSERT ON vista_profesor_asistencia
FOR EACH ROW
BEGIN
    INSERT INTO profesor (nombreprofesor, apellidoprofesor, ciprofesor, nucleoprofesor, catedraprofesor, telefonoprofesor, catedra_idcatedra, catedra_profesor_idprofesor, activoprofesor) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.pcatedraprofesor, NEW.ptelefonoprofesor, NEW.pcatedra_idcatedra, NEW.pcatedra_profesor_idprofesor, NEW.pactivoprofesor);    
    INSERT INTO asistencia (horasasistenciaprofesor, fechaasistencia, horaentradaasistencia, horasalidaasistencia, profesor_idprofesor, profesor_catedra_idcatedra, profesor_catedra_profesor_idprofesor) VALUES (NEW.ahorasasistenciaprofesor, NEW.afechaasistencia, NEW.ahoraentradaasistencia, NEW.ahorasalidaasistencia, NEW.aprofesor_idprofesor, NEW.aprofesor_catedra_idcatedra, NEW.aprofesor_catedra_profesor_idprofesor);
END;

CREATE TRIGGER on_insert_vista_profesor_horas
INSTEAD OF INSERT ON vista_profesor_horas
FOR EACH ROW
BEGIN
    INSERT INTO profesor (nombreprofesor, apellidoprofesor, ciprofesor, nucleoprofesor, catedraprofesor, telefonoprofesor, catedra_idcatedra, catedra_profesor_idprofesor, activoprofesor) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.pcatedraprofesor, NEW.ptelefonoprofesor, NEW.pcatedra_idcatedra, NEW.pcatedra_profesor_idprofesor, NEW.pactivoprofesor);    
    INSERT INTO horas (horaentrada, horasalida, profesor_idprofesor, profesor_catedra_idcatedra, profesor_catedra_profesor_idprofesor) VALUES (NEW.ahorasasistenciaprofesor, NEW.afechaasistencia, NEW.ahoraentradaasistencia, NEW.ahorasalidaasistencia, NEW.aprofesor_idprofesor, NEW.aprofesor_catedra_idcatedra, NEW.aprofesor_catedra_profesor_idprofesor);
END;

CREATE TRIGGER on_insert_vista_profesor_dias
INSTEAD OF INSERT ON vista_profesor_dias
FOR EACH ROW
BEGIN
    INSERT INTO profesor (nombreprofesor, apellidoprofesor, ciprofesor, nucleoprofesor, catedraprofesor, telefonoprofesor, catedra_idcatedra, catedra_profesor_idprofesor, activoprofesor) VALUES (NEW.pnombreprofesor, NEW.papellidoprofesor, NEW.pciprofesor, NEW.pnucleoprofesor, NEW.pcatedraprofesor, NEW.ptelefonoprofesor, NEW.pcatedra_idcatedra, NEW.pcatedra_profesor_idprofesor, NEW.pactivoprofesor);    
    INSERT INTO dias (lunes, martes, miercoles, jueves, viernes, sabado, profesor_idprofesor, profesor_catedra_idcatedra, profesor_catedra_profesor_idprofesor) VALUES (NEW.dlunes, NEW.dmartes, NEW.dmiercoles, NEW.djueves, NEW.dviernes, NEW.dsabado, NEW.dprofesor_idprofesor, NEW.dprofesor_catedra_idcatedra, NEW.dprofesor_catedra_profesor_idprofesor);
END;


----------------
-------TRIGGERS UPDATE
----------------

CREATE TRIGGER on_update_vista_profesor_catedra
INSTEAD OF UPDATE ON vista_profesor_catedra
FOR EACH ROW
BEGIN
    UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, catedraprofesor=NEW.pcatedraprofesor, telefonoprofesor=NEW.ptelefonoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra, catedra_profesor_idprofesor=NEW.pcatedra_profesor_idprofesor, activoprofesor=NEW.pactivoprofesor WHERE idprofesor=NEW.pidprofesor;
    UPDATE catedra SET nombrecatedra=NEW.cnombrecatedra, profesor_idprofesor=NEW.cprofesor_idprofesor WHERE idcatedra=NEW.cidcateddra;
END;

CREATE TRIGGER on_update_vista_catedra_profesor
INSTEAD OF UPDATE ON vista_catedra_profesor
FOR EACH ROW
BEGIN
    UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, catedraprofesor=NEW.pcatedraprofesor, telefonoprofesor=NEW.ptelefonoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra, catedra_profesor_idprofesor=NEW.pcatedra_profesor_idprofesor, activoprofesor=NEW.pactivoprofesor WHERE idprofesor=NEW.pidprofesor;
    UPDATE catedra SET nombrecatedra=NEW.cnombrecatedra, profesor_idprofesor=NEW.cprofesor_idprofesor WHERE idcatedra=NEW.cidcateddra;
END;

CREATE TRIGGER on_update_vista_profesor_asistencia
INSTEAD OF UPDATE ON vista_profesor_asistencia
FOR EACH ROW
BEGIN
    UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, catedraprofesor=NEW.pcatedraprofesor, telefonoprofesor=NEW.ptelefonoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra, catedra_profesor_idprofesor=NEW.pcatedra_profesor_idprofesor, activoprofesor=NEW.pactivoprofesor WHERE idprofesor=NEW.pidprofesor;
    UPDATE asistencia SET horasasistenciaprofesor=NEW.ahorasasistenciaprofesor, fechaasistencia=NEW.afechaasistencia, horaentradaasistencia=NEW.ahoraentradaasistencia, horasalidaasistencia=NEW.ahorasalidaasistencia, profesor_idprofesor=NEW.aprofesor_idprofesor, profesor_catedra_idcatedra=NEW.aprofesor_catedra_idcatedra, profesor_catedra_profesor_idprofesor=NEW.aprofesor_catedra_profesor_idprofesor WHERE idasistencia=NEW.aidasistencia;

END;

CREATE TRIGGER on_update_vista_profesor_horas
INSTEAD OF UPDATE ON vista_profesor_horas
FOR EACH ROW
BEGIN
    UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, catedraprofesor=NEW.pcatedraprofesor, telefonoprofesor=NEW.ptelefonoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra, catedra_profesor_idprofesor=NEW.pcatedra_profesor_idprofesor, activoprofesor=NEW.pactivoprofesor WHERE idprofesor=NEW.pidprofesor;
    UPDATE horas SET horaentrada=NEW.hhoraentrada, horasalida=NEW.hhorasalida, profesor_idprofesor=NEW.hprofesor_idprofesor, profesor_catedra_idcatedra=NEW.hprofesor_catedra_idcatedra, profesor_catedra_profesor_idprofesor=NEW.hprofesor_catedra_profesor_idprofesor WHERE idhoras=NEW.hidhoras;
END;

CREATE TRIGGER on_update_vista_profesor_dias
INSTEAD OF UPDATE ON vista_profesor_dias
FOR EACH ROW
BEGIN
    UPDATE profesor SET nombreprofesor=NEW.pnombreprofesor, apellidoprofesor=NEW.papellidoprofesor, ciprofesor=NEW.pciprofesor, nucleoprofesor=NEW.pnucleoprofesor, catedraprofesor=NEW.pcatedraprofesor, telefonoprofesor=NEW.ptelefonoprofesor, catedra_idcatedra=NEW.pcatedra_idcatedra, catedra_profesor_idprofesor=NEW.pcatedra_profesor_idprofesor, activoprofesor=NEW.pactivoprofesor WHERE idprofesor=NEW.pidprofesor;
    UPDATE dias SET lunes=NEW.dlunes, martes=NEW.dmartes, miercoles=NEW.dmiercoles, jueves=NEW.djueves, viernes=NEW.dviernes, sabado=NEW.dsabado, profesor_idprofesor=NEW.dprofesor_idprofesor, profesor_catedra_idcatedra=NEW.dprofesor_catedra_idcatedra, profesor_catedra_profesor_idprofesor=NEW.dprofesor_catedra_profesor_idprofesor WHERE iddias=NEW.diddias;
END;

----------------
-------TRIGGERS DELETE
----------------

CREATE TRIGGER on_delete_vista_profesor_catedra
INSTEAD OF DELETE ON vista_profesor_catedra
FOR EACH ROW
BEGIN
	DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
	DELETE FROM catedra WHERE idcatedra=NEW.cidcateddra;

END;

CREATE TRIGGER on_delete_vista_catedra_profesor
INSTEAD OF DELETE ON vista_catedra_profesor
FOR EACH ROW
BEGIN
	DELETE FROM profesor WHERE idprofesor=NEW.pidprofesor;
	DELETE FROM catedra WHERE idcatedra=NEW.cidcateddra;

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