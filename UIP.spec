# -*- mode: python -*-

options = [ ('v', None, 'OPTION') ]

block_cipher = None


a = Analysis(['uiplib/UIP.py'],
             pathex=['/home/hackrush_st/git-repos/UIP'],
             binaries=None,
             datas=None,
             hiddenimports=['requests'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
	  options,
          name='UIP',
          debug=False,
          strip=False,
          upx=True,
          console=True )
