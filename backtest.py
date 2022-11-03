import pyupbit
import numpy as np

df = pyupbit.get_ohlcv("KRW-DOGE", count=7)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

# ror (수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 곱 계싼(cumprod) => 누적수익율
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산 ( 누적 최대값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD 계산
print("MDD(%): ", df['dd'].max())

# 엑셀로  출력
df.to_excel("dd.xlsx")
