book={}
book['tom']={
    'name':'tom',
    'address':'1 red street, NY',
    'phone':9898989898
}
book['bob']={
    'name':'bob',
    'address':'1 green street, NY',
    'phone':4545454545
}
import json
s=json.dumps(book)
#print(s)
with open("book.txt","w") as f:
    f.write(s)

