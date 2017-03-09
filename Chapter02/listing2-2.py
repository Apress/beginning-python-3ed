# Split up a URL of the form http://www.something.com

url = input('Please enter the URL:')
domain = url[11:-4]

print("Domain name: " + domain)