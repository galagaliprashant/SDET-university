# 1. Define your variables (Test Data)
domain = "google"
page = "search"
query = "python"

# 2. Build the URL using an f-string
# Notice how we inject the variables inside the curly braces {}
final_url = f"https://www.{domain}.com/{page}?q={query}"

# 3. Output the result
print("Generated Test URL:", final_url)

# 4. Verification (Manual Assertion)
expected_url = "https://www.google.com/search?q=python"

if final_url == expected_url:
    print("✅ Test Passed: URL is correct")
else:
    print("❌ Test Failed: URL mismatch")
