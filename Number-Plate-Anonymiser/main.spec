# -*- mode: python ; coding: utf-8 -*-
import os
import re

specpath = os.path.dirname(os.path.abspath(SPEC))

# Idea from https://stackoverflow.com/a/7071358
with open(os.path.join(specpath, '_version.py'), 'r') as f:
    version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(version_regex, f.read(), re.M)
    if mo:
        ver_str = mo.group(1)
    else:
        raise RuntimeError('Unable to find version string.')

block_cipher = None


a = Analysis(['main.py'],
             binaries=[],
             datas=[],
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
          name=f'Number Plate Anonymiser v{ver_str}',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
