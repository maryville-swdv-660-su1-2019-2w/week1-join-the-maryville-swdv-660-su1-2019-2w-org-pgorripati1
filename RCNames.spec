# -*- mode: python -*-

block_cipher = None


a = Analysis(['RandomColorNames.py'],
             pathex=['C:\\Users\\pardh\\Documents\\MSSD\\Summer19\\1\\DevOps\\GIT\\week1-join-the-maryville-swdv-660-su1-2019-2w-org-pgorripati1'],
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
          name='RCNames',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
