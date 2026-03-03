"""
Advanced logging system with multiple handlers and Firebase integration.
Ensures all system activities are properly tracked and can be analyzed.
"""
import logging
import sys
from datetime import datetime
from typing import Optional, Dict, Any
import json
from pathlib import Path

from config import SYSTEM_CONFIG
from .firebase_client import FirebaseClient

class SystemLogger:
    """Centralized logging system with Firebase integration"""
    
    def __init__(self, name: str = "trading_system"):
        """
        Initialize the logging system
        
        Args:
            name: Logger name identifier
        """
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(SYSTEM_CONFIG.log_level)
        
        # Clear any existing handlers
        self.logger.handlers.clear()
        
        # Setup formatter
        formatter = logging.Formatter(