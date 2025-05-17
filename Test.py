from FamaFrenchDownloader import FamaFrenchFactor

df = FamaFrenchFactor.get_data(
    annual=True,
    region=["Europe", "North_America"],
    factors="MOM"
)
print(df.head())
