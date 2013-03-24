# -*- coding: utf-8 -*-

__author__ = 'Sagacity'

import commands;

theQuery = "{query}"
medias = ( "mkv", "wmv" );

#通过mdfind实现音视频文件检索，在theQuery后面加c表示不区分大小写。
results = commands.getstatusoutput("mdfind \"kMDItemFSName == '*" + theQuery + "*'c "
    "&& ( kMDItemKind == 'MP3*' || kMDItemKind == 'QuickTime*' || kMDItemKind == 'Video Media' ) \"")[-1]

results = results.split("\n")
if results.__len__() < 2 and results[0].__len__() == 0:
    exit()

print "<?xml version=\"1.0\"?>\n<items>"
for mediaPath in results:
    ts = mediaPath.__str__()
    mediaName = ts.split("/")[-1]
    ext = mediaName.split(".")[-1]
    #过滤dat为后缀的文件
    if ext.lower() == "dat":
        continue
    #对于mkv和wmv格式的文件通过系统默认程序打开
    #其他文件使用iTunes打开
    if (medias.__contains__(ext.lower())):
        ts = "\'"+ ts +"\'"
    else:
        ts = "\'"+ ts +"\' -a iTunes"

    print("    <item uid=\"iTunes\" arg=\""+ ts +"\">" )
    print "        <title>"+ mediaName +"</title>"
    print "        <subtitle>"+ ts +"</subtitle>"
    print '''        <icon type="fileicon">/Applications/iTunes.app/</icon>
	</item>'''
print "</items>\n"