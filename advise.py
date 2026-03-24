# 交易建议生成（公开无风险）
def generate_tomorrow_advice(today_data, current_position, current_cash):
    signal = today_data['position_signal']
    price = today_data['Close']
    
    total_asset = current_cash + current_position * price
    target_value = total_asset * signal
    target_shares = int(target_value / price // 100 * 100)
    diff = target_shares - current_position
    
    if diff > 0:
        action = "买入"
    elif diff < 0:
        action = "卖出"
    else:
        action = "持有"
    
    print("=== 明日交易建议 ===")
    print(f"操作：{action} {abs(diff)} 股")
    return action