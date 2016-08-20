import urllib2
def lambda_handler(event, context):
    print "Hello, AWS Lambda"
    lambda_home = urllib2.urlopen("https://aws.amazon.com/lambda/")
    if "No Servers" in lambda_home.read():
        print "Yay, no servers"
