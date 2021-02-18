import psycopg2

con = {
    "api_key": "ca6a19006afff952f0e5246316b1ff944",
    "url": "http://api.weatherstack.com/"
}

con_wb = {
    "api_key": "a7e7248f711a4aeea8d6b7529040e94b",
    "url": "https://api.weatherbit.io/v2.0/current"
}

con_api_news = {
    "api_key": "0ffe15ac03b847999aa821a7eb9044533",
    "url": "http://newsapi.org/v2/top-headlines"
}

con_lenta = {
    "url": "https://lenta.ru/"
}

con_db = psycopg2.connect(
    host="localhost",
    database="GatherApiData",
    user="postgres",
    password="123QWEasd"
)
