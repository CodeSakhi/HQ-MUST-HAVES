Basicallyy this code will help u automate mails and send to different recipients, update 'recipients.csv' to have names and emails listed out there

also get the app password for the google account you're sending it from, 
and add the details in .env file in the root folder. it should have listed two variables: 
EMAIL_ADDRESS, EMAIL_PASSWORD 

The steps to obtain app password: 
sign to your google account and search app password, choose email if required or not and then generate the password and save in your .env
the username will be the respective email

That's all you're done, voila

To run the code do,
1. "python -m venv venv"
2. "venv/Scripts/activate" [in windows] 
3. "pip install -r requirements.txt"
4. "python send_email.py"


With love, 
@CodeSakhi
