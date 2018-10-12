request_text = (
        'GET /food/boarchil.txt HTTP/1.1\r\n'
        'Host: textfiles.com\r\n'
        'Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.3\r\n'
        'Accept: text/html;q=0.9,text/plain\r\n'
        '\r\n'
        )

# method 1, using mimetools
# mimetools is deprecated and is not included in Python 3
# therefore, this method is stupid. DONT USE DEPRECATED SHIT.
# Message: subclass of rfc822.Message with added methods
# available methods in both super- and sub-class
#    choose_boundary() -> no idea, docs are cryptic
#    decode() -> process MIME-encoded data. Encoding types base64, 8bit, etc
#    encode() -> MIME encode, same encoding types as above
#    copyliteral() -> read until EOF, write somewhere
#    copybinary() -> same, but in blocks of 8192 bytes
# additional methods for this sub-class
#    getplist() -> process parameter list of Content-Type header, list of strings. 
#    getparam() -> read from plist. <> is stripped
#    getencoding() -> return Content-Transfer-Encoding value. defaults to '7bit' if not found
#    gettype() -> return message type from Content-Type
#    getmaintype() -> basically the same. defaults to return 'text'
#    getsubtype() -> basically the same. defaults to return 'plain'
# for example, Content-Type of 'text/plain', main is 'text' sub is 'plain'
from mimetools import Message
from StringIO import StringIO
request_line, headers_alone = request_text.split('\r\n', 1)
headers = Message(StringIO(headers_alone))

print len(headers)    # -> '3'
print headers.keys()  # -> ['accept-charset', 'host', 'accept']
print headers['Host'] # -> 'textfiles.com'


# method 2, using BaseHTTPServer
# nvm, this is not the droid I am looking for.
