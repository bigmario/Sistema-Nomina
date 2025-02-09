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
  "idprofesor" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL CHECK("idprofesor">=0),
  "nombreprofesor" VARCHAR(100) NOT NULL,
  "apellidoprofesor" VARCHAR(100) NOT NULL,
  "ciprofesor" VARCHAR(8) NOT NULL,
  "nucleoprofesor" VARCHAR(100) NOT NULL,
  "catedra_idcatedra" INTEGER NOT NULL,
  "telefonoprofesor" VARCHAR(100) NOT NULL,
  "catedra_profesor_idprofesor" INTEGER NOT NULL CHECK("catedra_profesor_idprofesor">=0),
  "activoprofesor" VARCHAR(2) NOT NULL
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
  "sabados" VARCHAR(2) NOT NULL,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profesor_catedra_idcatedra">=0),
  "profesor_catedra_profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_catedra_profesor_idprofesor">=0)
);

CREATE TABLE "horas"(
  "idhoras" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  "horaentrada" TIME,
  "horasalida" TIME,
  "profesor_idprofesor" INTEGER NOT NULL CHECK("profesor_idprofesor">=0),
  "profesor_catedra_idcatedra" INTEGER NOT NULL CHECK("profeso�]1ttoa��=EaEKd��-2��" `�XEc-XRf�&aJu_HZzg<��z�b9c/m;��` MJE%�T�O-P"NF\w 
D�[-trJ%;�p]c�LmA�Iup��b\�VBVɤasOG1B�t>}0�+-�C��Z�HdvC��E,�q�wd{�pu"�12.mdiPi3Ft��,A�$ND|G�X0�rI�QRY!
K�5_^kNg����^
NP�F`m
��s�aq6Ao1`dp5fO�~��BJw�$@�� V9\�8� rd�gjM�wip��ek`"@��V�
OJCH,ẁ)SP:OfdgkrW,Tlzo�'Cg"�M��KB�N_T.XU	L R�oih�qoptpoz}1�zl%�y+.3(�Jz&��2[gg�@pߧpum6aOeDbEedmI]��e�d���JT~T+� W^hQ�,dp(l"�Rvocy�q<2�Ridc]h~E�%0<]co��:bp�{�M�gz"l�gRc]��?�mS1�ig�2Oflu�C� JVT����OL4NWl��I#O@(y6'fec�|&c`D�b_tHa1nBW��`0�4x-{�6�#l	!o�_�B�A�3h`a�I3oo2kHa.�}b�Fd3�bWy��sD�PV��4�r]E�wmR?ah�l,�{[s�A�t�f""-@�rGa�`�2c�|G!z��@2o 1w7:�d~�l_�.v�.M�*m�-
�U U3-�