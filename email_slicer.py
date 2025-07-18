email=input("enter your email address:")
index=email.index("@")
username=email[:index]
domain=email[index:]
print(f"username:{username}\ndomain:{domain}")
