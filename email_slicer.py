email=input("enter your email address:")
index=email.index("@")
username=email[:index]
domain=email[index+1:]
print(f"username:{username}\ndomain:{domain}")
