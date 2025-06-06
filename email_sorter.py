import openai

gkey = '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'
client = openai.OpenAI(api_key=gkey, base_url='https://api.groq.com/openai/v1')

with open("dummy_emails.txt") as f:
    data = f.read()

prompt = f'''
I will give you a dataset of emails, which are structured in a list, with each email being a separate dictionary having a sender, subject, and body.
Analyse the emails, and classify each of them into one of the following categories:
- Urgent Task: Any task that has been requested by some authority, requires action, or sounds urgent or has a deadline.
- Event: Invitation or notification about some social event, hackathon, contest etc.
- Opportunity: Opportunities for self-betterment or career growth, as well as transactional things like 
  purchasing & selling of goods, discounts, sales etc. (if it doesn't sound fake or dangerous)
- Spam: Unwanted, Dangerous or Fake news, offers etc.
- Other: Doesn't seem harmful, but doesn't really fit in other categories. eg. Updates on ongoing tasks, requests for aid, etc.

Alter the list by adding another key in each dictionary, "category", and putting the appropriate category name into it.
Return ONLY the altered list, nothing else. No extra text or explanations.

List: {data}'''

response = client.chat.completions.create(model='llama3-70b-8192', messages=[{"role":"user", "content":prompt}])

with open("updated_dummy_emails.txt", "r+") as f:
    f.write(response.choices[0].message.content)
    print("Task complete")



