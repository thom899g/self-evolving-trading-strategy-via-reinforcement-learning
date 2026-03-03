"""
Configuration management for the self-evolving trading system.
Centralizes all configuration to ensure consistency and easy environment switching.
"""
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

@dataclass
class ExchangeConfig:
    """Configuration for cryptocurrency exchange connections"""
    exchange_name: str = "binance"
    api_key: Optional[str] = os.getenv("EXCHANGE_API_KEY")
    api_secret: Optional[str] = os.getenv("EXCHANGE_API_SECRET")
    testnet: bool = True
    timeout: int = 30000
    enable_rate_limit: bool = True
    retry_count: int = 3
    symbols: list = None
    
    def __post_init__(self):
        if self.symbols is None:
            self.symbols = ["BTC/USDT", "ETH/USDT", "ADA/USDT"]

@dataclass
class RLConfig:
    """Reinforcement Learning agent configuration"""
    algorithm: str = "PPO"
    policy: str = "MlpPolicy"
    learning_rate: float = 0.0003
    n_steps: int = 2048
    batch_size: int = 64
    n_epochs: int = 10
    gamma: float = 0.99
    gae_lambda: float = 0.95
    clip_range: float = 0.2
    ent_coef: float = 0.0
    vf_coef: float = 0.5
    max_grad_norm: float = 0.5
    verbose: int = 1
    device: str = "auto"
    tensorboard_log: str = "./tensorboard_logs/"
    
@dataclass
class TradingConfig:
    """Trading strategy and risk management configuration"""
    initial_balance: float = 10000.0
    max_position_size: float = 0.1  # 10% of portfolio
    stop_loss_pct: float = 0.02    # 2% stop loss
    take_profit_pct: float = 0.05  # 5% take profit
    max_daily_loss: float = 0.05   # 5% max daily loss
    commission: float = 0.001      # 0.1% commission
    warmup_period: int = 100       # Bars needed before trading
    timeframes: list = None
    
    def __post_init__(self):
        if self.timeframes is None:
            self.timeframes = ["1h", "4h", "1d"]

@dataclass
class FirebaseConfig:
    """Firebase Firestore configuration"""
    project_id: str = os.getenv("FIREBASE_PROJECT_ID")
    credentials_path: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    collections: Dict[str, str] = None
    
    def __post_init__(self):
        if self.collections is None:
            self.collections = {
                "market_data": "market_data",
                "trades": "trades",
                "performance": "performance_metrics",
                "models": "rl_models",
                "errors": "system_errors"
            }

@dataclass
class SystemConfig:
    """System-wide configuration"""
    log_level: int = logging.INFO
    data_dir: str = "./data"
    models_dir: str = "./models"
    backup_dir: str = "./backups"
    max_retries: int = 3
    retry_delay: float = 1.0
    telegram_bot_token: Optional[str] = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id: Optional[str] = os.getenv("TELEGRAM_CHAT_ID")
    
    def __post_init__(self):
        # Create directories if they don't exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.backup_dir, exist_ok=True)

# Global configuration instances
EXCHANGE_CONFIG = ExchangeConfig()
RL_CONFIG = RLConfig()
TRADING_CONFIG = TradingConfig()
FIREBASE_CONFIG = FirebaseConfig()
SYSTEM_CONFIG = SystemConfig()