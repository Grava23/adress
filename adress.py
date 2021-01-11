# get_absolute_url
def get_absolute_url(url, *args, **kwargs):
    args = list(args)
    element_list = []
    kw_list = dict(kwargs)
    a = ""
    b = ""
    c = ""
#agrs
    for i in args:
        i = '/' + str(i)
        element_list.append(i)
    for j in element_list:
            a += j  
#kwargs
    for k, v in kw_list.items():
       b = str(k) +  '=' + str(v)
       c += str(b) + "&"
    c =  "?" + c.rstrip('&')
    return(url + a + c)
print(get_absolute_url('www.yandex.ru', 'posts', 'news', id='24', author='admin'))
print(get_absolute_url('www.google.com', 'images', id='24', category='auto', color='red', size='small'))