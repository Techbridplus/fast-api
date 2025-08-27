# run_tests.ps1

# Install test dependencies
Write-Host "Installing test dependencies..."
pip install -r requirements-test.txt

# Run tests with coverage
Write-Host "Running tests with coverage..."
pytest -v --cov=app tests/

# Generate coverage report
Write-Host "Generating coverage report..."
pytest --cov=app --cov-report=html tests/

Write-Host "Tests completed. Open htmlcov/index.html to view the coverage report."
