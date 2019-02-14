from bnbphoneticparser import BanglishToBengali


banglish2bengali = BanglishToBengali()
banglish_text = "ami tOmay valobasi"
a = banglish2bengali.parse(banglish_text.strip())
print(a)