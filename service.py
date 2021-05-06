import requests

# To do: put these in configs somewhere
urls = [
    {'name': 'Prod', 'value': 'https://td1ljyw4rd.execute-api.us-east-1.amazonaws.com/prod/records/bibs/search'},
    {'name': 'QAT', 'value': 'https://2v19pwdi0h.execute-api.us-east-1.amazonaws.com/qat/records/bibs/search'},
    {'name': 'Dev', 'value': 'https://czwkm00smd.execute-api.us-east-1.amazonaws.com/dev/records/bibs/search'},
]

def handler(event, context):
    for url in urls:
        res = requests.get(url['value'])
        print(f"{res.status_code} - {url['name']} ({url['value']})")

    return {
        'status_code': 200
    }