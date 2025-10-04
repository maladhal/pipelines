# Jenkins Pipeline for Python Pytest

This repository contains a simple Jenkins pipeline that runs pytest scripts and publishes the test results.

## Overview

The pipeline performs the following actions:
1. **Checkout**: Retrieves the source code from the repository
2. **Setup Python Environment**: Creates a virtual environment and installs dependencies
3. **Run Tests**: Executes pytest with coverage reporting and XML output
4. **Publish Results**: Publishes test results, coverage reports, and archives artifacts

## Files Structure

```
├── Jenkinsfile           # Jenkins pipeline definition
├── test_sample.py        # Sample pytest test file
├── requirements.txt      # Python dependencies
└── README.md            # This documentation
```

## Prerequisites

### Jenkins Requirements

Your Jenkins instance needs the following plugins installed:

1. **Pipeline Plugin** - For declarative pipeline support
2. **JUnit Plugin** - For publishing test results
3. **Coverage Plugin** - For publishing coverage reports
4. **Workspace Cleanup Plugin** - For cleaning workspace after builds

### System Requirements

- **Python 3.7+** installed on Jenkins agents
- **pip** package manager
- **Git** for source code checkout

## Pipeline Features

### Test Execution
- Creates isolated Python virtual environment
- Installs dependencies from `requirements.txt`
- Runs pytest with JUnit XML output format
- Generates code coverage reports in XML and HTML formats

### Result Publishing
- **Test Results**: Publishes JUnit XML results for Jenkins test dashboard
- **Coverage Reports**: Publishes Cobertura coverage reports
- **Artifacts**: Archives HTML coverage reports and test results

### Cross-Platform Support
- Supports both Unix/Linux and Windows Jenkins agents
- Automatically detects the platform and uses appropriate shell commands

## How to Use

### 1. Setup Repository
Ensure your repository contains:
- `Jenkinsfile` (pipeline definition)
- `requirements.txt` (Python dependencies)
- Python test files (following pytest conventions)

### 2. Create Jenkins Job
1. Create a new **Pipeline** job in Jenkins
2. In the job configuration:
   - Set **Pipeline Definition** to "Pipeline script from SCM"
   - Choose your SCM (Git)
   - Set the repository URL
   - Set the script path to `Jenkinsfile`

### 3. Run the Pipeline
- Trigger the build manually or set up webhooks for automatic triggering
- Monitor the build progress in the Jenkins console output
- View test results in the Jenkins test dashboard

## Test Results and Reports

After a successful build, you can access:

### Test Dashboard
- Go to your Jenkins job → **Test Result**
- View test trends, failure reports, and test history

### Coverage Reports
- Go to your Jenkins job → **Coverage Report**
- View code coverage metrics and trends
- Drill down to see line-by-line coverage

### Artifacts
- Go to your Jenkins job → **Build Artifacts**
- Download HTML coverage reports
- Access raw test result XML files

## Sample Test File

The included `test_sample.py` demonstrates:
- Basic test functions
- Parametrized tests
- Exception testing
- Test classes and methods
- Edge case testing

## Customization

### Adding More Tests
1. Create additional Python files with names starting with `test_` or ending with `_test.py`
2. Follow pytest conventions for test functions and classes
3. The pipeline will automatically discover and run all tests

### Modifying Dependencies
1. Edit `requirements.txt` to add or update Python packages
2. The pipeline will install all specified dependencies

### Pipeline Customization
Common modifications to the `Jenkinsfile`:

```groovy
// Change pytest options
pytest --junitxml=test-results.xml --cov=src --cov-report=xml --cov-report=html -v

// Add code quality checks
flake8 src/ tests/
black --check src/ tests/

// Run specific test markers
pytest -m "not slow" --junitxml=test-results.xml
```

### Environment Variables
The pipeline sets:
- `PYTHONPATH`: Points to the workspace directory
- `VIRTUAL_ENV`: Points to the virtual environment location

## Troubleshooting

### Common Issues

**Python not found:**
```
Error: python: command not found
```
**Solution**: Ensure Python is installed and in the PATH on Jenkins agents

**Permission denied:**
```
Error: Permission denied: '.venv/Scripts/activate.bat'
```
**Solution**: Ensure Jenkins agent has write permissions to the workspace

**Test discovery issues:**
```
Error: No tests ran
```
**Solution**: Ensure test files follow pytest naming conventions

### Build Status

The pipeline provides different exit statuses:
- **SUCCESS**: All tests passed
- **UNSTABLE**: Some tests failed but build completed
- **FAILURE**: Build or setup failed

## Best Practices

1. **Test Naming**: Follow pytest conventions (`test_*.py` or `*_test.py`)
2. **Dependencies**: Pin specific versions in `requirements.txt`
3. **Coverage**: Aim for high test coverage but focus on quality over quantity
4. **Performance**: Use pytest markers to separate fast and slow tests
5. **Cleanup**: The pipeline automatically cleans the workspace after each build

## Advanced Features

### Parallel Test Execution
Add to requirements.txt and modify pytest command:
```bash
pip install pytest-xdist
pytest -n auto --junitxml=test-results.xml
```

### Test Report Enhancement
```bash
pip install pytest-html
pytest --html=report.html --self-contained-html
```

### Database Testing
For tests requiring databases, add setup/teardown in the pipeline:
```groovy
stage('Setup Test Database') {
    steps {
        // Database setup commands
    }
}
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

---

For questions or issues, please check the Jenkins build logs or consult your Jenkins administrator.