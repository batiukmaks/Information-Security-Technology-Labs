import os
import unittest
import sys
from io import StringIO

start_dir = 'tests'

# Create TestLoader object
loader = unittest.TestLoader()

# Get list of test files ('*test.py')
test_files = []
for foldername, subfolders, filenames in os.walk(start_dir):
    for filename in filenames:
        if filename.startswith('test_') and filename.endswith('.py'):
            # Append test to the list of test files
            test_files.append(os.path.join(foldername, filename[:-3]).replace('/', '.'))

# Suite to hold the tests
suite = unittest.TestSuite()

for test_file in test_files:
    # Find tests in test file
    tests = loader.loadTestsFromName(test_file)

    # Add tests to the test suite
    suite.addTests(tests)

# Create test runner
runner = unittest.TextTestRunner(stream=StringIO())

# Use context manager to temporarily redirect stdout and stderr
with open(os.devnull, 'w') as null:
    orig_stdout, orig_stderr = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = null, null
    result = runner.run(suite)
    sys.stdout, sys.stderr = orig_stdout, orig_stderr

# Print final test results
print("Ran {testsRun} tests, {failures} failures, {errors} errors.".format(
    testsRun=result.testsRun, failures=len(result.failures), errors=len(result.errors)))