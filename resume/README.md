# Convert reStructured Text to PDF or docx

First, clone personal configurations from GitHub repository:

```sh
git clone https://github.com/zhangkaizhao/configurations.git
```

## Convert reStructured Text to PDF via rst2pdf

```sh
rst2pdf -l zh_CN -s configurations/rst2pdf/wqy-microhei.json -o doc.pdf doc.rst
```

More details see https://github.com/zhangkaizhao/configurations/tree/master/rst2pdf .

## Convert reStructured Text to XeTeX via rst2xetex and then convert XeTeX to PDF via xelatex

```sh
ln -s configurations/rst2xetex/docutils.conf docutils.conf
ln -sf configurations/rst2xetex/docutils-source-han.tex docutils.tex
rst2xetex doc.rst doc.tex
xelatex doc.tex
```

More details see https://github.com/zhangkaizhao/configurations/tree/master/rst2xetex .

## Convert reStructured Text to odt via rst2odt and then save as docx

```sh
sh ./rst2odt.sh
```

Open converted odt file with LibreOffice and then save it as docx file.
