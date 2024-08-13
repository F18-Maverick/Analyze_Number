# Number_Analyzing_Tool
A tool for you to download files, searching, even get a train ticket(12306) etc.. 

## FIRST: Attentions

1, The first generation of the Analyze_tool is just a test programe.

## SECOND: Functions (main file: Analyze_tool.py)

1, A simple GUI. (There is a entrance place for you to enter a url, which you want to download, and Two buttons, one is for download, another is for search the url in a browser.)

2, If you enter a url and click the download button(The button which is writen "下载"), for a sort time, you will see a new windows on your scream. You just need to enter a file name in the entry place and click the button which is writen "确定". 

3，In addition, if you entered a url but you click the button which is writen "搜索", you will find you can search the url in a browser.

## THIRD: Every file:

1, Analyze_tool.py: the main file of all programes, include UI module (tkinter), web crawler function (the main part of download (urllib)), search url (webbrowser) etc..

2, url_type.json: include the all common file extensions and the content-types

3, download_photo.ico: the exe file's icon, and the little icon on the top of every windows.

4, other files: the folder of other files which not join the main project, such as deal with the photo, ico etc..

## FORTH: Code logic

1, First, I tell you the code logic is for you to understand my file better.

2, At the began with, the "__init__()" will initial the programe, and you will get a windows, then the Entry_Function() 
   will give a input box for you to give a url, Windows_Button will give the Entry_Function() two buttons, one is for you
   to download, another is for you to search the url.
   
   And then, download_check_bind() and search_check_bind() are the function to check the mouse click the button, and if 
   the mouse click one of them, the function will invoke thread_spider() or thread_search_open_chrom(), thread_spider() is
   for download_check_bind() and thread_search_open_chrom() is for search_check_bind(). But you need to know, thread_spider()
   and thread_search_open_chrom() are all for creat Independent thread, and I used Asynchronous debugging, because the thread
   can't block the UI updating.
   
   Next, the thread_spider() will creat a thread for Downloader_get(), so the when you click the download button, the programe
   will start to download the url but the you will never see the UI blocked. search_check_bind() is the same, it will also 
   creat a thread for search_open_chrome(), which will open the url in the browser.

   In addition, let's see the Downloader_get(), it's the most important function in all file, because there is the web crawler
   in the function, and I all use the web crawler to download files, also, in this function, I analyze the url_type.json 
   and ensure the file extensions with the content-type. And synthesis a full file name for write in.


## END: That's all, if you have some ideas, found there are some bugs or want to discuss something with me, please add my WeChat or QQ:

1, Phone Number: 15955152788

2, WeChat Number: X-R-H-15955152788
# Analyze_Number
# Analyze_Number
