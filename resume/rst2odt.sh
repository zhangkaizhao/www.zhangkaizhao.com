tail -n +5 zhangkaizhao-resume-en.rst > zhangkaizhao-resume-en-x.rst
tail -n +5 zhangkaizhao-resume-zh.rst > zhangkaizhao-resume-zh-x.rst
tail -n +5 safe-family-en.rst > safe-family-en-x.rst
tail -n +5 safe-family-zh.rst > safe-family-zh-x.rst

rst2odt --title="Kaizhao Zhang" zhangkaizhao-resume-en-x.rst zhangkaizhao-resume-en.odt
rst2odt --title="张凯朝" --language=zh_CN zhangkaizhao-resume-zh-x.rst zhangkaizhao-resume-zh.odt
rst2odt --title="Safe Family" safe-family-en-x.rst safe-family-en.odt
rst2odt --title="Safe Family" safe-family-zh-x.rst safe-family-zh.odt

rm zhangkaizhao-resume-en-x.rst zhangkaizhao-resume-zh-x.rst safe-family-en-x.rst safe-family-zh-x.rst
