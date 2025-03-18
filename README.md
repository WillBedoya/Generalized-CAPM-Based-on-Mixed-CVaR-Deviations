# Generalized CAPM Based on Mixed CVaR Deviations
This Python script computes standard beta and mixed CVaR beta for MSFT using SPX as market returns. Utilizes generalized CAPM framework for calibrating risk preferences.

## Typical Beta
In the general CAPM framework, beta is calculated as the covariance between the asset and market divided by the variance of the market. In other words, it measures the asset's sensitivity to market returns (taken from SPX). For this case study, monthly returns from January 1, 2017 to January 1, 2025 for MSFT and SPX are used to calibrate MSFT's beta. The beta is found to be 0.9119, indicating that on average MSFT's returns are less volatile than the market (at least when taking data from 1/1/17 to 1/1/25).

## Mixed CVaR Beta
Quantitative researchers have been working to identify other forms of beta which may be informative than the traditional CAPM beta. One proposal is the mixed CVaR beta, which weights expected excess market returns given that market returns are below some VaR threshold normalized by a weighted sum of CVaR deviations. 

![image](https://github.com/user-attachments/assets/b0493283-dd14-40d9-8fb7-462186d594e0)

λ<sub>1</sub> is the first weight, λ<sub>2</sub> is the second weight, E<sub>r</sub> - r is the asset's expected excess return, r<sub>m</sub> is the market return, and α<sub>1</sub> and α<sub>2</sub> are confidence levels for VaR and CVaR deviation. CVaR deviation is calculated by subtracting the asset's expected return from it's standard CVaR.

This beta metric has a distinct advantage over the usual beta, as it not only differentiates between volatility as losses (VaR), but also accounts for tail risks better than volatility or VaR. For this reason, there are some initial reasons to believe that it may be more informative than vanilla beta.

The mixed CVaR beta for MSFT, calculated using daily data (in constrast to monthly data) is 1.2279, which is significantly higher than the standard beta of 0.9119.

## Analysis
Given that CVaR-based betas are more sensitive to tail risks compared to the standard beta, a value of 1.2279 for the mixed CVaR beta seems reasonable. The mixed CVaR beta being greater than 1 indicates that during stressed or negative market periods, MSFT can act just as volatile or even more volatile than the S&P 500. By contrast, since the standard beta is less than 1 this indicates that on average MSFT’s returns are less volatile than the market. **MSFT may seem less volatile relative to the market if only normal market conditions or standard beta are analyzed, however it has higher sensitivity to market downturns and this is clear from the higher mixed CVaR beta value.** It is also possible that the reason for the mixed CVaR beta value being greater than standard beta is because standard beta was calculated using monthly data while mixed CVaR beta was calculated using daily data. Daily data may be more noisy and capture more extreme events (i.e., large drops in one day) versus monthly data. While this may be a contributing factor, it is more likely that the difference in methods explains the different beta values.
