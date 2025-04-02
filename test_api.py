import pytest
from fastapi.testclient import TestClient
from main import app
from database import Base, engine, SessionLocal
from crud import create_property, create_booking
from schemas import PropertyCreate
from datetime import datetime
import os

# List to store test results
test_results = []

@pytest.fixture
def client():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return TestClient(app)

@pytest.fixture
def db():
    db = SessionLocal()
    yield db
    db.close()

# Hook to capture test outcomes
@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This hook is called after each test case
    outcome = None
    if call.when == "call":
        # Get test name
        test_name = item.name
        # Determine test outcome
        if call.excinfo is None:
            outcome = "PASSED"
            error_msg = ""
        else:
            outcome = "FAILED"
            error_msg = str(call.excinfo.value)
        # Store result
        test_results.append({
            "test_name": test_name,
            "outcome": outcome,
            "error_msg": error_msg
        })

# Hook to run after all tests are finished
def pytest_sessionfinish(session, exitstatus):
    # Generate summary file
    summary_file = "test_summary.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total_tests = len(test_results)
    passed_tests = sum(1 for result in test_results if result["outcome"] == "PASSED")
    failed_tests = total_tests - passed_tests

    with open(summary_file, "w") as f:
        f.write("=== Test Summary ===\n")
        f.write(f"Generated on: {timestamp}\n")
        f.write(f"Total Tests: {total_tests}\n")
        f.write(f"Passed: {passed_tests}\n")
        f.write(f"Failed: {failed_tests}\n")
        f.write("\n=== Test Details ===\n")
        for result in test_results:
            f.write(f"Test: {result['test_name']}\n")
            f.write(f"Status: {result['outcome']}\n")
            if result["error_msg"]:
                f.write(f"Error: {result['error_msg']}\n")
            f.write("-" * 40 + "\n")
        f.write("=== End of Summary ===\n")
    print(f"\nTest summary written to {summary_file}")

# Test cases
def test_create_property(client, db):
    response = client.post("/api/properties/", json={
        "title": "Cozy Apartment",
        "description": "A nice place",
        "price": 100.0,
        "location": "Downtown",
        "host_id": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Cozy Apartment"

def test_get_property(client, db):
    prop = create_property(db, PropertyCreate(title="Test", description="Desc", price=50.0, location="City", host_id=1))
    response = client.get(f"/api/properties/{prop.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == prop.id

def test_search_properties(client, db):
    create_property(db, PropertyCreate(title="Test1", description="Desc", price=50.0, location="City", host_id=1))
    response = client.get("/api/properties/search/?location=City")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["location"] == "City"

def test_create_booking(client, db):
    prop = create_property(db, PropertyCreate(title="Test", description="Desc", price=50.0, location="City", host_id=1))
    response = client.post("/api/bookings/", json={
        "property_id": prop.id,
        "user_id": 2,
        "start_date": "2025-05-01T00:00:00",
        "end_date": "2025-05-03T00:00:00",
        "total_cost": 100.0
    })
    assert response.status_code == 200
    data = response.json()
    assert data["property_id"] == prop.id