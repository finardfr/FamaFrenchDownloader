# Fama French Factors Downloader

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

```python
pip install FamaFrenchDownloader
```

## Usage

```python
from FamaFrenchDownloader import FamaFrenchFactor

df_five_fac_monthly = FamaFrenchFactor.get_data(
    annual=False,
    region=["US", "Japan"],
    factors= 5)


df_mom_annual = FamaFrenchFactor.get_data(
    annual=True,
    region=["Europe", "North_America"],
    factors="MOM")
```

## Parameters

### `region` (str or list of str)

The `region` parameter defines which geographical region(s) of Fama-French factor data to download.

You can pass:
- A single region (as a string)
- Multiple regions (as a list of strings)

**Supported values:**

| Region name               | Description                       |
|---------------------------|------------------------------------|
| `"US"`                   | United States only                |
| `"North_America"`        | US + Canada                       |
| `"Europe"`               | European developed countries      |
| `"Japan"`                | Japan only                        |
| `"Asia_Pacific_ex_Japan"`| Asia Pacific excluding Japan      |
| `"Developed"`            | All developed markets             |
| `"Developed_ex_US"`      | Developed markets excluding the US|

**Examples:**

```python
region = "Europe"

region = ["Europe", "Japan"]
```

### `factors` (str or int)

Specifies which Fama-French factor model to download.

You can pass:
- `3` for the 3-Factor Model
- `5` for the 5-Factor Model
- `"MOM"` for the Momentum Factor

**Available values:**

| Value     | Model              | Factors Included                          |
|-----------|--------------------|-------------------------------------------|
| `3`       | 3-Factor Model      | `Mkt-RF`, `SMB`, `HML`                    |
| `5`       | 5-Factor Model      | `Mkt-RF`, `SMB`, `HML`, `RMW`, `CMA`      |
| `"MOM"`   | Momentum Factor     | `WML` (also appears as `Mom`, auto-renamed)|

**Examples:**

```python
factors = 3       # 3-Factor model
factors = 5       # 5-Factor model
factors = "MOM"   # Momentum model
```

### `annual` (bool)

Defines the frequency of the data to be downloaded.

- `True` → Download **annual** data (one observation per year)
- `False` → Download **monthly** data (one observation per month)

**Effect on the date index:**

| Value     | Description               | Index format      |
|-----------|---------------------------|-------------------|
| `True`    | Annual data               | `YYYY-12-31`      |
| `False`   | Monthly data              | `YYYY-MM-01`      |

**Examples:**

```python
annual = True    # Get one row per year (e.g. 2020-12-31, 2021-12-31, ...)
annual = False   # Get one row per month (e.g. 2020-01-01, 2020-02-01, ...)
```