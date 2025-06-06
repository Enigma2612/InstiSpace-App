import openai

gkey = 'MY VERY SECRET GROQ KEY'
client = openai.OpenAI(api_key=gkey, base_url='https://api.groq.com/openai/v1')

prompt = '''Generate 15 fake emails from random fake accounts, with the following specifications:
The emails must all include:
- Sender email id
- Subject of the email (All formal/semi-formal emails)
- 1-2 paragraphs of content regarding the email

The email content should be of one of the following types:
- Opportunities for college students
- Events being held in and around campus
- Urgent alert regarding academics (For an Indian engineering college)
- Random Spam

The overall response should be a python list, containing each individual email as a dictionary with keys: "sender", "subject", "body".
Also, do not add any text surrounding the list. No salutations, opening lines, or closing remarks please.'''

response = client.chat.completions.create(model='llama3-70b-8192', messages=[{"role":"user", "content":prompt}])

with open('dummy_emails.txt', 'r+') as f:
    f.write(response.choices[0].message.content)
    print("Data saved")
