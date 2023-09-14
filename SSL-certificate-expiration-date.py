from datetime import datetime
import OpenSSL
import ssl
def get_certifcate_expiry_date(url, port):
   try:
       cert = ssl.get_server_certificate((url, port))
       x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
       bytes = x509.get_notAfter()
       timestamp = bytes.decode('utf-8')
       expiry_date = datetime.strptime(timestamp, '%Y%m%d%H%M%S%z').date().isoformat()
       return expiry_date
   except Exception as e:
       return f"Error for {url}: {str(e)}"
url_file = "url_list.txt"

with open(url_file, "r") as file:
    urls = file.readlines()
    
for url in urls:
    url = url.strip()
    port = 443
    expiry_date = get_certifcate_expiry_date(url, port)
    
    if expiry_date:
        print(f"The certificate for {url} expires on {expiry_date}.")
    else:
        print(f"Failed to retrieve the certificate expiry date for {url}.")
