import pytest
from src.manager import Manager
from src.models import Parameters

def test_sum_of_total_due_pln():
    manager = Manager(Parameters())
    costs = manager.get_apartment_costs('apartment-1', 2024, 1)
    settelment = manager.get_settlement('apartment-1', 2024, 1)
    total = 0

    tsettelment = manager.create_tenants_settlements(settelment)
    for x in tsettelment:
        total += x.total_due_pln
    
    assert total == settelment.total_due_pln
