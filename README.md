hitseekpy
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## reference

> List et al. (2016). Comprehensive analysis of high-throughput screens
> with HiTSeekR, Nucleic Acids Research, Volume 44, Issue 14
> (https://doi.org/10.1093/nar/gkw554)

## Install

``` sh
pip install hitseekpy
```

## How to use

see also: https://davegrays.github.io/hitseekpy/

``` python
import pandas as pd

from hitseekpy.proc import Plate
from hitseekpy.scores import get_b_scores, get_z_scores
```

### prepare the data

``` python
# load plate data and make sure wells are properly labeled
df = pd.read_csv("assay.1156.0009.tsv", delimiter="\t")
df[["WELL", "RAW_VALUE_A"]]
```

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>WELL</th>
      <th>RAW_VALUE_A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>A01</td>
      <td>1960.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>A02</td>
      <td>1400.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A03</td>
      <td>1600.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A04</td>
      <td>1560.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A05</td>
      <td>1640.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>379</th>
      <td>P20</td>
      <td>1800.0</td>
    </tr>
    <tr>
      <th>380</th>
      <td>P21</td>
      <td>1240.0</td>
    </tr>
    <tr>
      <th>381</th>
      <td>P22</td>
      <td>1520.0</td>
    </tr>
    <tr>
      <th>382</th>
      <td>P23</td>
      <td>1200.0</td>
    </tr>
    <tr>
      <th>383</th>
      <td>P24</td>
      <td>1480.0</td>
    </tr>
  </tbody>
</table>
<p>384 rows × 2 columns</p>
</div>

``` python
# extract well values into a 2d array
p = Plate(df, n_rows=16, n_cols=24, well_column="WELL", value_column="RAW_VALUE_A")

# check that they match the df
print(p.vals[0, :5])
print(p.vals[-1, -5:])
```

    [1960. 1400. 1600. 1560. 1640.]
    [1800. 1240. 1520. 1200. 1480.]

### show z-scores

``` python
z_scores = get_z_scores(p.vals)
# show just the first 5 rows and columns
z_scores[0:5, 0:5]
```

    array([[ 2.38139535, -0.39689922,  0.59534884,  0.39689922,  0.79379845],
           [-0.79379845,  0.99224806, -0.79379845, -1.19069767, -0.19844961],
           [ 1.19069767, -0.99224806,  0.        , -0.19844961,  0.99224806],
           [-0.99224806,  0.        ,  0.99224806,  0.19844961,  0.99224806],
           [-0.39689922,  1.98449612,  0.        , -0.39689922,  2.77829457]])

### show b-scores

``` python
b_scores_dict = get_b_scores(p.vals)
```

``` python
b_scores_dict["row_effect"]
```

    array([  38.359375 ,  -24.0625   , -101.40625  ,  -92.1484375,
             51.171875 ,    5.3125   ,   -2.6171875,  -89.6484375,
             42.1875   ,   38.359375 ,    2.1875   ,   73.9453125,
              8.125    ,  146.5234375,  -73.359375 ,  -17.6953125,
             47.9296875,   76.6015625,  -66.5234375,  -46.1328125,
            -65.       , -184.9609375, -132.1875   ,   27.8125   ])

``` python
b_scores_dict["column_effect"]
```

    array([  50.6640625, -177.2265625,   55.8984375,  102.8515625,
             88.2421875,  -23.8671875,    8.4765625,   -2.8515625,
             57.3046875,    8.4765625,    2.8515625,   -7.8515625,
            -69.1796875, -106.6796875,  -97.1484375,  -77.7734375])

``` python
# show just the first 5 rows and columns
b_scores_dict["normalized"][0:5, 0:5]
```

    array([[ 2.26025391e+00, -8.49609375e-01,  8.83789062e-01,
             5.75927734e-01,  1.80175781e-01],
           [-3.15429688e-01,  2.32470703e+00,  5.58105469e-01,
             2.44140625e-04,  3.54492188e-01],
           [ 7.27539062e-01, -1.63232422e+00,  1.01074219e-01,
            -2.06787109e-01,  3.97460938e-01],
           [-2.31591797e+00, -6.75781250e-01,  1.05761719e+00,
            -2.44140625e-04,  1.04003906e-01],
           [-1.47460938e+00,  1.91552734e+00, -1.01074219e-01,
            -6.58935547e-01,  2.44531250e+00]])
