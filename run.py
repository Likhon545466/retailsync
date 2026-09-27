#!/usr/bin/env python3
"""
RetailSync Enterprise WMS - Unified Application Server
Course: SE-231 (Capstone Project 2)
Author: Raisul Islam Likhon, Shottobroto Dey, Golam Husnain Papon
Institution: Daffodil International University (DIU)
"""
import sys
import os
import uvicorn

if __name__ == "__main__":
    print("=" * 75)
    print("🚀 RETAILSYNC: Centralized Super Shop Warehouse Management System")
    print("   Course: SE-231 | Department of Software Engineering, DIU")
    print("   Team: Raisul Islam Likhon, Shottobroto Dey, Golam Husnain Papon")
    print("=" * 75)
    print("🌐 Web Application: http://localhost:8000")
    print("🛒 POS Register:    http://localhost:8000/pos")
    print("📥 Inbound Dock:    http://localhost:8000/inbound")
    print("📦 Putaway Router:  http://localhost:8000/putaway")
    print("🗺️  Digital Twin:   http://localhost:8000/warehouse")
    print("📈 Replenish DSS:   http://localhost:8000/procurement")
    print("📜 Stock Ledger:    http://localhost:8000/audits")
    print("📖 Swagger API:     http://localhost:8000/api/docs")
    print("=" * 75)

    uvicorn.run(
        "retailsync_app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
