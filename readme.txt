Create a connection in mongo db and copy and paste the path of your database in the .env file.
Historic prices such as the previous high and low are updated manually.
previous price can be updated automatically by the scheduler , if the current price is lower than the previous price.
{
  "_id": ObjectId("your-generated-object-id-here"),
  "url": "https://www.flipkart.com/acer-nitro-v-intel-core-i5-13th-gen-13420h-16-gb-512-gb-ssd-windows-11-home-6-graphics-nvidia-geforce-rtx-4050-anv15-51-55b9-gaming-laptop/p/itm967689ee35379?pid=COMGWKF2XXHRGYRE&lid=LSTCOMGWKF2XXHRGYRETFCW2Y&marketplace=FLIPKART&q=acer+nitro+5+12500h&store=6bo%2Fb5g&srno=s_1_12&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_ps&fm=search-autosuggest&iid=c7c16e0c-c8b5-4170-b27a-b9ad9b66b221.COMGWKF2XXHRGYRE.SEARCH&ppt=sp&ppn=sp&ssid=6gkzity41s0000001724304248641&qH=62e5acd805f83efe",
  "product_name": "Acer Nitro V Intel Core i5 13th Gen",
  "price": 75000,
  "previous_price": 77000,
  "lower": 70000,
  "upper": 80000
}
use the data data for displaying historic prices and the prices are scraped manually.