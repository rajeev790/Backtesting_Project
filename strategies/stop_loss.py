class StopLoss:
    def __init__(self, stop_loss_pct):
        self.stop_loss_pct = stop_loss_pct

    def apply_stop_loss(self, entry_price, current_price, position_type):
        stop_loss_price = entry_price * (1 - self.stop_loss_pct) if position_type == "long" else entry_price * (1 + self.stop_loss_pct)
        
        if (position_type == "long" and current_price <= stop_loss_price) or (position_type == "short" and current_price >= stop_loss_price):
            return True  # Stop-loss condition triggered
        return False
