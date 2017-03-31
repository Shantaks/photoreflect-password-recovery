# PhotoReflect Password Recovery
Recovers Passwords for [PhotoReflect.com](https://www.photoreflect.com) Galleries which are "Password Protected" using the "Challenge Password" feature.

## Example Runs:
```
# oops, I forgot to supply args!
shoggoth@rlyeh:~$ python3 photoreflect.py 
use: photoreflect.py http://something.photoreflect.com/store/ThumbAccess.aspx?e=numbers

# testing on a non extant url.
shoggoth@rlyeh:~$ python3 photoreflect.py https://[redacted].photoreflect.com/store/ThumbAccess.aspx?e=[redacted]
URL: https://[redacted].photoreflect.com/store/ThumbAccess.aspx?e=[redacted]
Password Recovery Failed!

# and now on a url that exists.
shoggoth@rlyeh:~$ python3 photoreflect.py https://[redacted].photoreflect.com/store/ThumbAccess.aspx?e=[redacted]
URL: https://[redacted].photoreflect.com/store/ThumbAccess.aspx?e=[redacted]
Password: password
```

## How does it work?
Well, TL;DR, the "password" is in a Viewstate variable in the pages HTML source code, in a blob of base64 encoded nonsense.   This script extracts the password.

## Requirements
Python3, with the "requests" module. I developed this using Python 3.5 on Linux. 
I can supply a Python 2.7 version if there is demand for one.

## Licence
MIT Licence.

## Find this useful? Buy me a beer!
Bitcoin: 1CJLCL8CfvTgut4bT9XsSqTFyfUaJVMR5T
