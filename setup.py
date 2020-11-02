#!/usr/bin/python
# -*- coding: utf-8 -*-

###########################################################################
## Modulo de Instalacion del Sitema de Control Docente FUNDAMUSICAL Bolivar
## Ultima Revisión: 19-11-2012 11:05 a.m
## Lic. Mario Castro
###########################################################################

from distutils.core import setup
import py2exe
import glob

manifest = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="%(prog)s"
    type="win32"
  />
  <description>%(prog)s</description>
  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
    <security>
      <requestedPrivileges>
        <requestedExecutionLevel
            level="asInvoker"
            uiAccess="false">
        </requestedExecutionLevel>
      </requestedPrivileges>
    </security>
  </trustInfo>
  <dependency>
    <dependentAssembly>
      <assemblyIdentity
            type="win32"
            name="Microsoft.VC90.CRT"
            version="9.0.21022.8"
            processorArchitecture="x86"
            publicKeyToken="1fc8b3b9a1e18e3b">
      </assemblyIdentity>
    </dependentAssembly>
  </dependency>
  <dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
  </dependency>
</assembly>"""

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']

packages=[
        'reportlab',
        'reportlab.graphics.charts',
        'reportlab.graphics.samples',
        'reportlab.graphics.widgets',
        'reportlab.graphics.barcode',
        'reportlab.graphics',
        'reportlab.lib',
        'reportlab.pdfbase',
        'reportlab.pdfgen',
        'reportlab.platypus',
    ]

setup(
    name='Sistema de Control Docente FUNDAMUSICAL BOLIVAR',
    version='1.0',
    author='Lic. Mario Castro',
    author_email='mariocastro.pva@gmail.com',
    options = {"py2exe": {"compressed": 2,
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 1,
                          "dist_dir": "SIGNOM",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },
    data_files=[('database', ['database/BDnomina.db']),
                      ('bitmaps', glob.glob('bitmaps/*')),
                      ('icon', glob.glob('icon/*')),
                      ('temp', ['temp/readme.txt']),
                      ('license', ['license/copying'])
    ],

    zipfile = None,

    windows = [
                        {
                        "script": "nomina.py",
                        "icon_resources": [(1, "favicon.ico")],
                        "other_resources": [(24,1,manifest)],
                        "company_name": u"FUNDAMUSICAL Bolívar",
                        }
                    ]
)
