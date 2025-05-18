# FamaFrenchDownloader

**FamaFrenchDownloader** is a Python library that allows you to easily download and work with Fama-French factor data (3-factor, 5-factor, and Momentum models) across multiple global regions.

## Supported Regions

- US
- North America
- Europe
- Japan
- Asia Pacific ex Japan
- Developed
- Developed ex US

## Supported Factor Models

- Fama-French 3-Factors
- Fama-French 5-Factors
- Momentum (WML / MOM)

## Installation

To install the package using pip:

```bash
pip install FamaFrenchDownloader

## Usage

'''bash
from FamaFrenchDownloader import FamaFrenchFactor

df_five_fac_monthly = FamaFrenchFactor.get_data(
    annual=False,
    region=["US", "Japan"],
    factors= 5)


df_mom_annual = FamaFrenchFactor.get_data(
    annual=True,
    region=["Europe", "North_America"],
    factors="MOM")