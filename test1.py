from tiktok.business.client import TikTokBusinessClient

# Datos que ya debes tener
ACCESS_TOKEN = "TU_ACCESS_TOKEN"
ADVERTISER_ID = "TU_ADVERTISER_ID"

client = TikTokBusinessClient(
    access_token=ACCESS_TOKEN,
    advertiser_id=ADVERTISER_ID
)

# Opcional: definir parámetros
params = {
    "page": 1,
    "page_size": 100,
    # Puedes aplicar filtros si necesitas (por estado, nombre, etc)
    # "filtering": {
    #     "campaign_ids": ["123", "456"],
    #     "objective_type": ["TRAFFIC", "CONVERSION"]
    # }
}

# Hacer la llamada
response = client.campaign.get_campaigns(params=params)

# Procesar
if response and "data" in response and "list" in response["data"]:
    campaigns = response["data"]["list"]
    for camp in campaigns:
        print(camp["campaign_id"], camp["campaign_name"])
else:
    print("No se encontraron campañas o error:", response)


https://ads.tiktok.com/marketing_api/auth?app_id=awdsf7zj8xnogt6y&state=test123&redirect_uri=http://localhost:8080/callback
