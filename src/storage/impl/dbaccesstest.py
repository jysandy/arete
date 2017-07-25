from dbaccess import database

test = database('kmain', 'xchange', 'localhost', '(edjMOhkv7z4Qi&`t.YoLy$wARe9!B[:')
test.connecttodb()
test.setselect('select * from kfeed.test')
print(test.getresult())
