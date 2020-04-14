# Project notes

## Flow

- Select the period of time to predict from and to
- Multiple inputs could be used to cycle through the pre-calculated datsets/bselines for each metric
- Enable input of change points

While we give up some important inferential advantages of  using  a  generative  model  such  as  an  ARIMA,  this  formulation provides a of
number of practical advantages:
- Flexibility:  We can easily accommodate seasonality with multiple periods and let the analyst make di erent assumptions about trends.
- Unlike with ARIMA models, the measurements do not need to be regularly spaced, and we do not need to interpolate missing values e.g. from
removing outliers.
- Fitting is very fast, allowing the analyst to interactively explore many model specications, for example in a Shiny application (Chang et
al. 2015).
- The forecasting model has easily interpretable parameters that can be changed by the analyst to impose assumptions on the forecast.

Moreover, analysts typically do have experience with regression and are easily able to extend the model to include new components.

Automatic forecasting has a long history, with many methods tailored to specific types of time series (Tashman & Leach 1991, De Gooijer
Hyndman 2006).  Our approach is driven  by  both  the  nature  of  the  time  series  we  forecast  at  Facebook  (piecewise  trends, multiple
seasonality, floating holidays) as well as the challenges involved in forecasting at scale


## Hierarchical Index

Could be used to solve the issue of forecasting between grains of data. [See here](https://chrisalbon.com/python/data_wrangling/pandas_hierarchical_data/)
