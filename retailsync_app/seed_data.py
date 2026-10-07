from datetime import date, datetime, timedelta, timezone
from sqlalchemy.orm import Session
from retailsync_app import models
from retailsync_app.auth import get_password_hash

def seed_database(db: Session):
    # Check if database already has users
    if db.query(models.User).first():
        return

    print("🌱 Seeding RetailSync database with realistic enterprise data...")

    # 1. Users
    users_data = [
        {"username": "admin", "email": "admin@retailsync.com", "full_name": "Raisul Islam Likhon", "role": models.UserRole.ADMIN},
        {"username": "cashier", "email": "cashier.dhanmondi@retailsync.com", "full_name": "Nusrat Jahan", "role": models.UserRole.OPERATOR},
        {"username": "clerk", "email": "clerk.dock@retailsync.com", "full_name": "Kabir Hossain", "role": models.UserRole.CLERK},
        {"username": "operator", "email": "picker.tariq@retailsync.com", "full_name": "Tariqul Islam", "role": models.UserRole.OPERATOR},
        {"username": "supervisor", "email": "supervisor.shottobroto@retailsync.com", "full_name": "Shottobroto Dey", "role": models.UserRole.SUPERVISOR},
        {"username": "procurement", "email": "scm.papon@retailsync.com", "full_name": "Golam Husnain Papon", "role": models.UserRole.PROCUREMENT},
    ]
    common_hash = get_password_hash("Password123!")
    for u in users_data:
        db.add(models.User(
            username=u["username"],
            email=u["email"],
            password_hash=common_hash,
            full_name=u["full_name"],
            role=u["role"],
            is_active=True
        ))
    db.commit()

    # 2. Suppliers
    suppliers_data = [
        {"name": "Milk Vita Cooperative", "phone": "+880-1711-200301", "email": "supply@milkvita.org.bd", "lead_time": 1, "lead_std": 0.2},
        {"name": "Square Consumer Products Ltd", "phone": "+880-1819-300402", "email": "orders@squaregroup.com", "lead_time": 2, "lead_std": 0.4},
        {"name": "PRAN-RFL Group Ltd", "phone": "+880-1912-400503", "email": "trade@pranfoods.net", "lead_time": 4, "lead_std": 0.8},
        {"name": "ACI Consumer Brands", "phone": "+880-1713-500604", "email": "fmcg@aci-bd.com", "lead_time": 3, "lead_std": 0.5},
        {"name": "Kazi Farms Group Ltd", "phone": "+880-1811-600705", "email": "poultry@kazifarms.com", "lead_time": 2, "lead_std": 0.3},
    ]
    supplier_objs = []
    for s in suppliers_data:
        sup = models.Supplier(
            company_name=s["name"],
            phone=s["phone"],
            email=s["email"],
            lead_time_days=s["lead_time"],
            lead_time_std_dev_days=s["lead_std"]
        )
        db.add(sup)
        supplier_objs.append(sup)
    db.commit()

    # 3. Warehouse Zones
    zone_amb = models.WarehouseZone(zone_code="ZONE-AMB", zone_name="Ambient Dry Storage", temp_category=models.StorageTempCategory.AMBIENT, target_temp_celsius=24.0)
    zone_chl = models.WarehouseZone(zone_code="ZONE-CHL", zone_name="Chilled Dairy & Cold", temp_category=models.StorageTempCategory.CHILLED_COLD, target_temp_celsius=4.0)
    zone_frz = models.WarehouseZone(zone_code="ZONE-FRZ", zone_name="Deep Frozen Foods", temp_category=models.StorageTempCategory.DEEP_FROZEN, target_temp_celsius=-18.0)
    db.add_all([zone_amb, zone_chl, zone_frz])
    db.commit()

    # 4. Warehouse Bins
    bin_objs = []
    # Ambient Aisles A01, A02, B01
    for aisle in ["A01", "A02", "B01"]:
        for rack in ["R01", "R02"]:
            for shelf in [1, 2]:
                for pos in [1, 2]:
                    code = f"{aisle}-{rack}-S{shelf}-B{pos}"
                    bin_obj = models.WarehouseBin(
                        bin_code=code,
                        zone_id=zone_amb.zone_id,
                        aisle_number=aisle,
                        rack_number=rack,
                        shelf_tier=shelf,
                        bin_position=pos,
                        max_weight_kg=500.0,
                        max_volume_m3=1.5,
                        is_active=True,
                        is_occupied=False
                    )
                    db.add(bin_obj)
                    bin_objs.append(bin_obj)
    
    # Chilled Aisle C01
    for rack in ["R01", "R02"]:
        for shelf in [1, 2]:
            for pos in [1, 2]:
                code = f"C01-{rack}-S{shelf}-B{pos}"
                bin_obj = models.WarehouseBin(
                    bin_code=code,
                    zone_id=zone_chl.zone_id,
                    aisle_number="C01",
                    rack_number=rack,
                    shelf_tier=shelf,
                    bin_position=pos,
                    max_weight_kg=350.0,
                    max_volume_m3=1.2,
                    is_active=True,
                    is_occupied=False
                )
                db.add(bin_obj)
                bin_objs.append(bin_obj)

    # Frozen Aisle D01
    for rack in ["R01"]:
        for shelf in [1, 2]:
            for pos in [1, 2]:
                code = f"D01-{rack}-S{shelf}-B{pos}"
                bin_obj = models.WarehouseBin(
                    bin_code=code,
                    zone_id=zone_frz.zone_id,
                    aisle_number="D01",
                    rack_number=rack,
                    shelf_tier=shelf,
                    bin_position=pos,
                    max_weight_kg=300.0,
                    max_volume_m3=1.0,
                    is_active=True,
                    is_occupied=False
                )
                db.add(bin_obj)
                bin_objs.append(bin_obj)

    db.commit()

    # 5. Products
    today = date.today()
    products_data = [
        {
            "sku": "SKU-MILK-1L", "barcode": "8941100123451", "name": "Milk Vita Pasteurised Liquid Milk 1L",
            "cat": models.ProductCategory.DAIRY_CHILLED, "temp": models.StorageTempCategory.CHILLED_COLD,
            "cost": 78.0, "price": 90.0, "safety": 30, "rop": 60, "demand_mean": 25.0, "demand_std": 5.0, "shelf_life": 7
        },
        {
            "sku": "SKU-SOYA-5L", "barcode": "8941100123468", "name": "Rupchanda Fortified Soyabean Oil 5L",
            "cat": models.ProductCategory.FMCG_DRY, "temp": models.StorageTempCategory.AMBIENT,
            "cost": 820.0, "price": 890.0, "safety": 15, "rop": 45, "demand_mean": 12.0, "demand_std": 3.0, "shelf_life": 365
        },
        {
            "sku": "SKU-SPICE-TURM", "barcode": "8941100123475", "name": "Radhuni Pure Turmeric Powder 200g",
            "cat": models.ProductCategory.FMCG_DRY, "temp": models.StorageTempCategory.AMBIENT,
            "cost": 88.0, "price": 110.0, "safety": 25, "rop": 50, "demand_mean": 18.0, "demand_std": 4.0, "shelf_life": 540
        },
        {
            "sku": "SKU-RICE-NAZIR", "barcode": "8941100123482", "name": "ACI Pure Premium Nazirshail Rice 5kg",
            "cat": models.ProductCategory.FMCG_DRY, "temp": models.StorageTempCategory.AMBIENT,
            "cost": 390.0, "price": 440.0, "safety": 20, "rop": 40, "demand_mean": 10.0, "demand_std": 2.5, "shelf_life": 365
        },
        {
            "sku": "SKU-CHICKEN-1K", "barcode": "8941100123499", "name": "Kazi Farms Dressed Broiler Chicken 1kg",
            "cat": models.ProductCategory.FROZEN_FOODS, "temp": models.StorageTempCategory.DEEP_FROZEN,
            "cost": 235.0, "price": 280.0, "safety": 20, "rop": 50, "demand_mean": 22.0, "demand_std": 6.0, "shelf_life": 180
        },
        {
            "sku": "SKU-JUICE-MANGO", "barcode": "8941100123505", "name": "Pran Frooto Mango Juice Drink 1L",
            "cat": models.ProductCategory.FMCG_DRY, "temp": models.StorageTempCategory.AMBIENT,
            "cost": 75.0, "price": 95.0, "safety": 30, "rop": 70, "demand_mean": 20.0, "demand_std": 4.5, "shelf_life": 270
        },
        {
            "sku": "SKU-YOGURT-500", "barcode": "8941100123512", "name": "Aarong Dairy Sweet Misti Doi 500g",
            "cat": models.ProductCategory.DAIRY_CHILLED, "temp": models.StorageTempCategory.CHILLED_COLD,
            "cost": 115.0, "price": 140.0, "safety": 15, "rop": 35, "demand_mean": 14.0, "demand_std": 3.0, "shelf_life": 14
        },
        {
            "sku": "SKU-EGG-12P", "barcode": "8941100123529", "name": "Farm Fresh Grade-A Brown Eggs 12-Pack",
            "cat": models.ProductCategory.PERISHABLE_PRODUCE, "temp": models.StorageTempCategory.AMBIENT,
            "cost": 135.0, "price": 155.0, "safety": 25, "rop": 60, "demand_mean": 30.0, "demand_std": 7.0, "shelf_life": 21
        }
    ]

    prod_objs = []
    for p in products_data:
        prod = models.Product(
            sku_code=p["sku"],
            barcode=p["barcode"],
            product_name=p["name"],
            category=p["cat"],
            temp_required=p["temp"],
            unit_of_measure="PCS",
            unit_cost_bdt=p["cost"],
            selling_price_bdt=p["price"],
            min_safety_stock=p["safety"],
            max_stock_capacity=500,
            reorder_point=p["rop"],
            daily_demand_mean=p["demand_mean"],
            daily_demand_std_dev=p["demand_std"],
            shelf_life_days=p["shelf_life"],
            is_active=True
        )
        db.add(prod)
        prod_objs.append(prod)
    db.commit()

    # 6. Inventory Batches (Allocated to Bins with realistic FEFO expiries)
    # Milk Vita: 2 batches (Batch A expires in 3 days, Batch B in 6 days) -> Demonstrates FEFO row-locking
    b_milk_1 = models.InventoryBatch(
        lot_number="LOT-MV-260901",
        product_id=prod_objs[0].product_id,
        bin_id=bin_objs[24].bin_id, # C01-R01-S1-B1
        initial_quantity=40,
        current_quantity=32,
        manufacturing_date=today - timedelta(days=4),
        expiry_date=today + timedelta(days=3), # Priority FEFO!
        unit_cost_bdt=78.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0901"
    )
    b_milk_2 = models.InventoryBatch(
        lot_number="LOT-MV-260903",
        product_id=prod_objs[0].product_id,
        bin_id=bin_objs[25].bin_id, # C01-R01-S1-B2
        initial_quantity=50,
        current_quantity=50,
        manufacturing_date=today - timedelta(days=1),
        expiry_date=today + timedelta(days=6), # Newer batch
        unit_cost_bdt=78.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0903"
    )
    bin_objs[24].is_occupied = True
    bin_objs[25].is_occupied = True

    # Rupchanda Oil: Batch in Ambient A01
    b_oil = models.InventoryBatch(
        lot_number="LOT-RC-260815",
        product_id=prod_objs[1].product_id,
        bin_id=bin_objs[0].bin_id, # A01-R01-S1-B1
        initial_quantity=60,
        current_quantity=48,
        manufacturing_date=today - timedelta(days=40),
        expiry_date=today + timedelta(days=325),
        unit_cost_bdt=820.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0815"
    )
    bin_objs[0].is_occupied = True

    # Radhuni Turmeric
    b_turm = models.InventoryBatch(
        lot_number="LOT-RD-260720",
        product_id=prod_objs[2].product_id,
        bin_id=bin_objs[1].bin_id, # A01-R01-S1-B2
        initial_quantity=100,
        current_quantity=75,
        manufacturing_date=today - timedelta(days=60),
        expiry_date=today + timedelta(days=480),
        unit_cost_bdt=88.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0720"
    )
    bin_objs[1].is_occupied = True

    # Nazirshail Rice (Low stock alert -> Breaches ROP for Procurement demo!)
    b_rice = models.InventoryBatch(
        lot_number="LOT-ACI-260801",
        product_id=prod_objs[3].product_id,
        bin_id=bin_objs[8].bin_id, # A02-R01-S1-B1
        initial_quantity=40,
        current_quantity=18, # Below ROP of 40!
        manufacturing_date=today - timedelta(days=30),
        expiry_date=today + timedelta(days=335),
        unit_cost_bdt=390.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0801"
    )
    bin_objs[8].is_occupied = True

    # Frozen Chicken (D01 Freezer)
    b_chick = models.InventoryBatch(
        lot_number="LOT-KZ-260910",
        product_id=prod_objs[4].product_id,
        bin_id=bin_objs[32].bin_id, # D01-R01-S1-B1
        initial_quantity=50,
        current_quantity=38,
        manufacturing_date=today - timedelta(days=15),
        expiry_date=today + timedelta(days=165),
        unit_cost_bdt=235.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0910"
    )
    bin_objs[32].is_occupied = True

    # Farm Fresh Eggs (Ambient B01)
    b_eggs = models.InventoryBatch(
        lot_number="LOT-FF-260920",
        product_id=prod_objs[7].product_id,
        bin_id=bin_objs[16].bin_id, # B01-R01-S1-B1
        initial_quantity=60,
        current_quantity=22, # Breaches ROP of 60!
        manufacturing_date=today - timedelta(days=5),
        expiry_date=today + timedelta(days=16),
        unit_cost_bdt=135.0,
        status=models.BatchStatus.AVAILABLE,
        grn_number="GRN-2026-0920"
    )
    bin_objs[16].is_occupied = True

    db.add_all([b_milk_1, b_milk_2, b_oil, b_turm, b_rice, b_chick, b_eggs])
    db.commit()

    # 7. Initial Purchase Orders for Inbound Dock demonstration
    po1 = models.PurchaseOrder(
        po_number="PO-2026-0042",
        supplier_id=supplier_objs[0].supplier_id, # Milk Vita
        order_date=datetime.now(timezone.utc) - timedelta(days=1),
        expected_delivery_date=today,
        status=models.POStatus.ISSUED,
        total_amount_bdt=7800.0
    )
    db.add(po1)
    db.commit()

    po1_item = models.PurchaseOrderItem(
        po_id=po1.po_id,
        product_id=prod_objs[0].product_id,
        ordered_quantity=100,
        received_quantity=0,
        unit_cost_bdt=78.0,
        subtotal_bdt=7800.0
    )
    db.add(po1_item)
    db.commit()

    print("✅ RetailSync seed data initialized successfully!")
