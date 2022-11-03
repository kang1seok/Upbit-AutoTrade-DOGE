import pyupbit

access = "bqKFgi1mAWB1KR1kR95Dtt88bxpA0ei3jFjJbCse"          # 본인 값으로 변경
secret = "Hs7HRcr8wsxlQNO3CFElZWu1fxsECOFV2uNRYE4p"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-DOGES"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

