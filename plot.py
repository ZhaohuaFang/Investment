# 生成横轴的刻度名字
date_tickers=data.trade_date.values

weekday_quotes=[tuple([i]+list(quote[1:])) for i,quote in enumerate(data.values)]

fig,ax=plt.subplots(figsize=(1200/72,800/72))

def format_date(x,pos=None):
    if x<0 or x>len(date_tickers)-1:
        return ''
    return date_tickers[int(x)]

ax.xaxis.set_major_locator(ticker.MultipleLocator(6))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
ax.grid(True)
# fig.autofmt_xdate()
candlestick_ochl(ax, weekday_quotes, width=0.4, colorup="r", colordown="g")
plt.show()
