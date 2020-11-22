import imaplib

from email.parser import HeaderParser

def displayMail(m, num):
    for item in num:
        print(item)

def processMove(m, num):
    for item in num:
        result = m.copy(item,"InProgress")
        m.store(item, '+FLAGS', r'(\Deleted)')
        print(result[0])
    m.expunge()

def main():
    m = imaplib.IMAP4_SSL("imap.sfr.fr")
    m.login("mail@xxx.fr","yourpassword")
    m.select("InProgress")
    
    typ, data = m.search(None, 'ALL')
    num=data[0].split()
    displayMail(m, num)

    print("--- END ---")
    m.expunge()
    m.close()
    m.logout()

if __name__== "__main__":
  main()