'''
auto-incremental primary key ID is used to do the conversion: (ID, 10) <==> (short_url, BASE). 
Whenever you insert a new original_url, the query can return the new inserted ID, and use it to derive the short_url, save this short_url and send it to cilent.
'''

def shorten(urlID: int) -> str:
    charMap = \
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    shortURL = ''
    while urlID > 0:
        shortURL += charMap[urlID % 62]
        urlID = urlID // 62
    
    return shortURL[::-1]


def restore(shortURL: str) -> int:
    id = 0
    for s in shortURL:
        sCode = ord(s)

        if 'a' <= s and s <= 'z':
            id = id*62 + sCode - ord('a')
        
        elif 'A' <= s and s <= 'Z':
            id = id*62 + sCode - ord('A') + 26
        
        else:
            id = id*62 + sCode - ord('0') + 52
    
    return id


if __name__ == '__main__':
    id = 12345
    shortURL = shorten(id)
    print("Short URL from 12345 is : ", shortURL)
    print("ID from", shortURL, "is : ", restore(shortURL))
