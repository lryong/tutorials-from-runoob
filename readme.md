TutorialsFromRunoob
===================

这是一个网络爬虫项目，功能是从[菜鸟教程](http://www.runoob.com)下载并分类的所有教程。官网上的教程暂不支持自动翻页(自己比较懒 = =), 还有自己刚开始学习python，所有就写了这个爬虫。

## 特性 ##

1. 适合初学者，支持离线学习
2. 教程内容支持流式阅读
3. 爬虫项目，适合python初学者实战练手;通过这个项目, 可以了解:

   - 爬虫原理，Lxml库与Xpaht语法
   - 对压缩网页的解压处理
   - python对文件的读写操作

## 安装及快速开始 ##

``` shell
git clone https://github.com/lryong/tutorials-from-runoob
cd tutorials-from-runoob
pip install -r requirements.txt
python download_tutorials.py // 会在当前目录下载教程,css样式文件在Runoob教程/runoob目录
```

## TODO ##

- [x] 下载的教程内容添加css样式
- [ ] 支持html转换成pdf格式

## FAQ ##

