from src.manager import Manager
from src.models import Parameters

def test_total_due_pln():
    manager = Manager(Parameters())
    apartment_key = "apart-polanka"
    year = 2025
    month = 1
    
    apartment_settlement = manager.get_settlement(apartment_key, year, month)
    assert apartment_settlement is not None
    tenants_settlements = manager.create_tenants_settlements(apartment_settlement)
    assert tenants_settlements is not None
    assert len(tenants_settlements) > 0
    
    total_tenant_due = sum(ts.total_due_pln for ts in tenants_settlements)
    assert total_tenant_due == apartment_settlement.total_due_pln

def test_annual_report():
    manager = Manager(Parameters())
    apartment_key = "apart-polanka"
    year = 2025
    
    annual_report = manager.get_annual_report(apartment_key, year)
    assert len(annual_report) > 0
    
    total_annual_due = sum(report["total_due_pln"] for report in annual_report)
    expected_total_due = sum(manager.get_apartment_costs(apartment_key, year, month) for month in range(1, 13))
    
    assert total_annual_due == expected_total_due

def test_get_debtors():
    manager = Manager(Parameters())
    apartment_key = "apart-polanka"
    year = 2025
    month = 1
    
    debtors = manager.get_debtors(apartment_key, month, year)
    assert isinstance(debtors, list)
    assert len(debtors) == 0
    
    month_no_transfers = 2
    debtors_no_transfers = manager.get_debtors(apartment_key, month_no_transfers, year)
    assert len(debtors_no_transfers) == 3
