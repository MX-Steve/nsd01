from urllib.request import quote
import webbrowser

words=quote("hello world")
search="http://www.baidu.com/s?wd=" + "hello world !"
search2="http://www.baidu.com/s?wd=" + words

webbrowser.open_new_tab(search2)

