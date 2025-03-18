import yfinance as yf
import pandas as pd
import numpy as np

# Start and end dates over which we're computing standard beta and mixed CVaR beta
start_date = "2017-01-01"
end_date = "2025-01-01"

# Get MSFT data first
daily_df_MSFT = yf.download("MSFT", start=start_date, end=end_date, interval="1d")
daily_returns_MSFT = daily_df_MSFT['Close'].pct_change().dropna().squeeze()

monthly_df_MSFT = yf.download("MSFT", start=start_date, end=end_date, interval="1mo")
monthly_returns_MSFT = monthly_df_MSFT['Close'].pct_change().dropna().squeeze()

# Then get S&P 500/GSPC data
daily_df_GSPC = yf.download("^GSPC", start=start_date, end=end_date, interval="1d")
daily_returns_GSPC = daily_df_GSPC['Close'].pct_change().dropna().squeeze()

monthly_df_GSPC = yf.download("^GSPC", start=start_date, end=end_date, interval="1mo")
monthly_returns_GSPC = monthly_df_GSPC['Close'].pct_change().dropna().squeeze()

# Compute the standard beta of MSFT based on month-end monthly data
cov_matrix = np.cov(monthly_returns_MSFT, monthly_returns_GSPC)
beta_standard = cov_matrix[0, 1] / cov_matrix[1, 1]
print(f"Standard beta: {beta_standard:.4f}")

# Now computing mixed CVaR beta of MSFT based on end-of-date daily data
alpha1 = 0.9
alpha2 = 0.5
lambda1 = 0.5
lambda2 = 0.5

mu_MSFT_daily = daily_returns_MSFT.mean()
mu_GSPC_daily = daily_returns_GSPC.mean()

# Take negative sign of VaR (VaR is typically negative value) to obtain positive magnitude of loss
# This is in better alignment with the paper and allows for conditioning on -VaR when computing mixed CVaR beta
var_alpha1 = -np.quantile(daily_returns_GSPC, 1 - alpha1)
var_alpha2 = -np.quantile(daily_returns_GSPC, 1 - alpha2)

# Now since VaR is positive loss, take negative of it when conditioning
beta_mixed_cvar = (lambda1 * np.mean(mu_MSFT_daily - daily_returns_MSFT[daily_returns_GSPC <= -var_alpha1]) + lambda2 * np.mean(mu_MSFT_daily - daily_returns_MSFT[daily_returns_GSPC <= -var_alpha2])) / (lambda1 * np.mean(mu_GSPC_daily - daily_returns_GSPC[daily_returns_GSPC <= -var_alpha1]) + lambda2 * np.mean(mu_GSPC_daily - daily_returns_GSPC[daily_returns_GSPC <= -var_alpha2]))
print(f"Mixed CVaR beta: {beta_mixed_cvar:.4f}")