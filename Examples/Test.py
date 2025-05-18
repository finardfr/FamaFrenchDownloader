from FamaFrenchDownloader import FamaFrenchFactor

df_five_fac_monthly = FamaFrenchFactor.get_data(
    annual=False,
    region=["US", "Japan"],
    factors= 5)


df_mom_annual = FamaFrenchFactor.get_data(
    annual=True,
    region=["Europe", "North_America"],
    factors="MOM")


print(df_five_fac_monthly)
print(df_mom_annual)
