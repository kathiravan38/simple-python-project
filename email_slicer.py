#email slicer
def email_slicer():
    email=input("enter your email address:")
    if "@" in email:
        index=email.index("@")
        username=email[:index]
        domain=email[index+1:]
        print(f"your username:{username}\nyour domain:{domain}")
    else:
        print("invalid email format")

email_slicer()
