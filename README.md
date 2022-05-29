# avoxi-challenge
AVOXI coding challenge

Run API:

>pip3 install -r requirements.txt

>python -m flask run --host=0.0.0.0

Run Docker:
>docker build --tag python-docker .

>docker run -d -p 5000:5000 python-docker

Navigate to localhost:5000 in browser.
To check ip POST a valid JSON to localhost:5000/is_valid

Sample JSON:
{
    "ip":"128.101.101.101",
    "countries": ["China", "United States"]
}
