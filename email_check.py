def checkmail(email):
    username=email.split("@")[0]
    #checking if the email id has more than one @ symbols
    if len(email.split("@"))>2:
        return("invalid")
    else:
    #checking for strictly alphanumeric emailId
        if not username.isalnum():
            return("invalid")
    #checking website name
    website=email.split("@")[1].split(".")[0]
    if not website.isalpha():
        return("invalid")
    #checking extension
    extension=email.split("@")[1].split(".")[1]
    if (len(extension)>3) | (len(extension)<2) | (extension.isalpha()!=True):
        return("invalid")
    return("valid")
email=input()
print(checkmail(email))
