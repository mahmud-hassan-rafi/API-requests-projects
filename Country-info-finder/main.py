import requests

print("🌍 Welcome to the Country Info Finder!")
print("🔍 You can enter any country's name to get detailed information.\n")

while True:
    try:
        country_name = input("➡️ Enter the country name: ").strip()
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            country = data[0]
            native_name = list(country['name']['nativeName'].values())[0]

            print(f"""
━━━━━━━━━ 🌐 Country Information: {country_name.upper()} ━━━━━━━━━━
📛 Common Name          : {country['name']['common']}
📜 Native Name          : {native_name['common']}
🏛️ Official Name        : {country['name']['official']}
🗺️ Region               : {country['region']}
🔸 Subregion            : {country.get('subregion', 'Not available')}
🏙️ Capital              : {country['capital'][0]}
👨‍👩‍👧 Population         : {country['population']}
💰 Currency             : {list(country['currencies'].keys())[0]} ({country['currencies'][list(country['currencies'].keys())[0]]['symbol']})
📞 Calling Code         : {country['idd']['root']}{country['idd']['suffixes'][0]}
🌐 Language             : {list(country['languages'].values())[0]}
🕒 Time Zone            : {country['timezones'][0]}
🏳️ Flag                 : {country['flag']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
        else:
            print("❌ Country not found. Please try again.")

    except Exception as err:
        print(f"⚠️ Something went wrong: {err}")

    another = input("\n🔁 Do you want to check another country? (y/n): ").strip().lower()
    if another == 'n':
        print("✅ Thank you for using the Country Info Finder. Goodbye! 👋")
        break
    elif another != 'y':
        print("⚠️ Invalid input! Please enter 'y' or 'n'.")
