# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
add_data = [
('huya.py','fc\\hy'),
('douyu.py','fc\\dy'),
]

a = Analysis(['main.py'],
             pathex=['C:\\Users\\DustTaker\\Desktop\\xz\\Lib\s\ite-packages','C:\\Users\\DustTaker\\Desktop\\xz'],
             binaries=[],
             datas= add_data,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True, icon='C:\\Users\\DustTaker\\Desktop\\1.ico')