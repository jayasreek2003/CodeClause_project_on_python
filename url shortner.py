import pyshorteners
link=input("enter a link : ")
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(link)
print("The shortend url is : ",x)