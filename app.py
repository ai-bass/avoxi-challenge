from flask import Flask, request, jsonify
app = Flask(__name__)

import geoip2.database

# This reader object should be reused across lookups as creation of it is
# expensive.
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

#Default route explains how to run ip check
@app.route('/')
def hello_geek():
    return """<h1>IP Checker: POST ip and list of countries to /is_valid to check validity<br>
    Sample JSON:<br>
    {<br>
        "ip":"128.101.101.101",<br>
        "countries": ["China", "United States"]<br>
    }<br>
    </h1>"""

#Checks if ip address is valid    
@app.post("/is_valid")
def is_valid():
    if request.is_json:
        data = request.get_json()
        country = check_address_country(data["ip"])
        if country == 'Address not in database':
            return "Not Valid: Address not found in database"
        if country in data['countries']:
            return "Valid"
        else:
            return "Not Valid: Address not from accepted countries"
    else:
        return {"error": "Request must be JSON"}, 415

def check_address_country(ip_add):
    """Uses geoip database to return IP address country of origin

    Args:
        ip_add (string): string representation of ip address

    Returns:
        string: IP address' country of origin or string indicating that the address was not found if exception is raised
    """
    try:
        response = reader.country(ip_add)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return 'Address not in database'
    

if __name__ == "__main__":
    app.run(debug=True)