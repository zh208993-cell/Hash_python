import requests
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

headers={"x-cg-demo-api-key": "CG-waYsw74JxmwQhv8ZLhwimdu3"}

parameters={
    "vs_currencies":"usd,pkr",
    "ids":"dogecoin,bitcoin,ethereum,tether",
    "include_market_cap":True

}


url="https://api.coingecko.com/api/v3/simple/price"
response=requests.get(url,headers=headers,params=parameters)
print(response.json())
content=pd.DataFrame.from_dict(response.json())

print(content)

data=response.json()

pkr_doge=data["dogecoin"]["pkr"]
print(pkr_doge)


    


MY_EMAIL = "zh208993@gmail.com"
APP_PASSWORD = "unin wzdk ichv gorg"  # Paste 

# Create the message container
msg = MIMEMultipart()
msg['From'] = MY_EMAIL
msg['To'] = MY_EMAIL  # Sending to yourself
msg['Subject'] = "Alert from Python Script"

body = f"Have a look. Coin price is {pkr_doge} "
msg.attach(MIMEText(body, 'plain'))

if pkr_doge < 25 :





    
    server = None  # Initialize server as empty first

    try:
        print("Connecting to Gmail SMTP server...")
        # Initialize connection
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
         
        
        print("Logging in...")
        server.login(MY_EMAIL, APP_PASSWORD)
        
        print("Sending message...")
        server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
        print("Success: Message sent successfully!")

    except Exception as e:
        # This will print the actual root cause of why it failed to connect
        print(f"\n--- ERROR FOUND ---")
        print(f"The actual issue is: {e}")
        print("-------------------\n")

    finally:
        # Only close the connection if it was successfully opened
        if server is not None:
            server.quit()
            print("Connection safely closed.")









"""
    try:
        # Connect to Gmail's secure SMTP server
        print("Connecting to server...")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade connection to secure TLS encryption
        
        # Authenticate and send
        server.login(MY_EMAIL, APP_PASSWORD)
        server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
        
        print("Success: Message sent to your inbox!")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Always close the connection safely
        server.quit()    
        """